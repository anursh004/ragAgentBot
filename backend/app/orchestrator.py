from typing import Any, Dict, List

from app.agents.guardrails_agent import GuardrailsAgent
from app.agents.ingestion_agent import IngestionAgent
from app.agents.intent_classification_agent import IntentClassificationAgent
from app.agents.knowledge_retrieval_agent import KnowledgeRetrievalAgent
from app.agents.memory_agent import MemoryAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.reasoning_correlation_agent import ReasoningCorrelationAgent
from app.agents.response_synthesis_agent import ResponseSynthesisAgent
from app.models import AgentEvent
from app.observability import event_stream


def serialize_events() -> List[AgentEvent]:
    return [
        AgentEvent(
            agent=event.agent,
            step=event.step,
            input={},
            output=event.payload,
        )
        for event in event_stream.all_events()
    ]


def run_orchestration(ticket: Dict[str, Any]) -> Dict[str, Any]:
    planner = PlannerAgent()
    ingestion = IngestionAgent()
    intent_agent = IntentClassificationAgent()
    retrieval_agent = KnowledgeRetrievalAgent()
    memory_agent = MemoryAgent()
    reasoning_agent = ReasoningCorrelationAgent()
    response_agent = ResponseSynthesisAgent()
    guardrails_agent = GuardrailsAgent()

    plan = planner.run(ticket)
    normalized = ingestion.run(ticket)
    intent_data = intent_agent.run(normalized)

    documents = retrieval_agent.run(normalized)
    episodic_memory = memory_agent.read("episodic")

    reasoning = reasoning_agent.run(intent_data, documents, episodic_memory)
    summary = f"Intent: {intent_data['intent']}, urgency: {intent_data['urgency']}"
    response = response_agent.run(
        {
            "summary": summary,
            "correlation": reasoning["correlation"],
            "recommendation": reasoning["recommendation"],
        }
    )

    confidence = 0.72 if intent_data["urgency"] == "high" else 0.6
    guardrails = guardrails_agent.run({"text": normalized["text"], "confidence": confidence})

    memory_agent.write("episodic", {"ticket_id": normalized["ticket_id"], "summary": summary})
    memory_agent.write("working", {"current_ticket": normalized})

    event_stream.log("Orchestrator", "plan", plan)

    return {
        "ticket_id": normalized["ticket_id"],
        "final_response": response["response"],
        "confidence": guardrails["confidence"],
        "escalated": guardrails["escalated"],
        "events": serialize_events(),
        "memories_written": ["episodic", "working"],
        "retrieved_documents": documents,
    }
