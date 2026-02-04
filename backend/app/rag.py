from typing import Any, Dict, List


def retrieve_documents(query: str) -> List[Dict[str, Any]]:
    return [
        {
            "document_id": "runbook-payment-gateway",
            "snippet": "If EU payment failures spike, check gateway health and latency.",
            "source": "runbook.pdf",
            "score": 0.87,
        },
        {
            "document_id": "incident-2024-06-12",
            "snippet": "Prior incident correlated with EU gateway timeouts.",
            "source": "incidents.md",
            "score": 0.79,
        },
    ]


def chunk_documents(documents: List[Dict[str, Any]], chunk_size: int, overlap: int) -> List[Dict[str, Any]]:
    chunks = []
    for doc in documents:
        snippet = doc["snippet"]
        for index in range(0, len(snippet), max(chunk_size - overlap, 1)):
            chunk_text = snippet[index : index + chunk_size]
            chunks.append({"document_id": doc["document_id"], "chunk": chunk_text})
    return chunks
