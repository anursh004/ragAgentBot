from fastapi import FastAPI

from app.models import OrchestratorResponse, TicketInput
from app.orchestrator import run_orchestration
from app.observability import event_stream

app = FastAPI(title="Collaborative Agents Support Co-Pilot")


@app.post("/orchestrate", response_model=OrchestratorResponse)
async def orchestrate(ticket: TicketInput) -> OrchestratorResponse:
    result = run_orchestration(ticket.model_dump())
    return OrchestratorResponse(**result)


@app.get("/events")
async def events() -> dict:
    return {"events": [event.__dict__ for event in event_stream.all_events()]}
