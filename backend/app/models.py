from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TicketInput(BaseModel):
    ticket_id: str
    text: str
    source: str = "support"
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AgentEvent(BaseModel):
    agent: str
    step: str
    input: Dict[str, Any]
    output: Dict[str, Any]


class OrchestratorResponse(BaseModel):
    ticket_id: str
    final_response: str
    confidence: float
    escalated: bool
    events: List[AgentEvent]
    memories_written: List[str]
    retrieved_documents: List[Dict[str, Any]]
    warnings: Optional[List[str]] = None
