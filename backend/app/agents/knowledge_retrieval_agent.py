from typing import Any, Dict, List

from app.observability import event_stream
from app.rag import retrieve_documents
from app.tools import run_tool


class KnowledgeRetrievalAgent:
    name = "Knowledge Retrieval Agent"

    def run(self, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        query = payload["text"]
        event_stream.log(self.name, "retrieval:start", {"query": query})
        documents = run_tool(self.name, "retrieve_documents", {"query": query}, retrieve_documents)
        event_stream.log(self.name, "retrieval:done", {"count": len(documents)})
        return documents
