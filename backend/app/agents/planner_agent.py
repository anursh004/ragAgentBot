from typing import Any, Dict

from app.observability import event_stream


class PlannerAgent:
    name = "Planner / Orchestrator Agent"

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        event_stream.log(self.name, "planning:start", payload)
        plan = {
            "serial": ["ingestion", "intent", "reasoning", "synthesis", "guardrails"],
            "parallel": ["retrieval", "memory_read"],
            "async": ["memory_write", "observability"],
        }
        event_stream.log(self.name, "planning:done", plan)
        return plan
