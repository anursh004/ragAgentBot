# Collaborative Agents Support Co-Pilot

This repository is a starter scaffold for a collaborative agent system aimed at support and incident response teams. It provides a clean architecture, explicit agent boundaries, and observable tool usage with a simple web UI.

## What this includes
- **Backend**: FastAPI service with explicit agent modules and an orchestrator.
- **Frontend**: Minimal streaming UI to show agent calls, execution steps, and responses.
- **Architecture**: Clear separation of retrieval, reasoning, response synthesis, and guardrails.
- **Observability**: Structured logs and in-memory event stream for UI.

## Quick start
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open `frontend/index.html` in a browser and point it at the backend URL.

## Key paths
- `backend/app/agents`: Individual agent implementations (one file per agent).
- `backend/app/orchestrator.py`: Planner/Orchestrator coordinating agents.
- `backend/app/observability.py`: Event stream for UI.
- `backend/app/rag.py`: Retrieval pipeline stub.
- `backend/app/memory_store.py`: Working, episodic, and semantic memory.

## Docker
```bash
docker compose up --build
```

## Notes
This scaffold is intended to be extended with a production-grade RAG stack, durable storage, and full test coverage. The current code focuses on establishing the required agent boundaries, tool logging, and UI observability.
