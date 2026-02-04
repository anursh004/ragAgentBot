from typing import Any, Dict

from app.observability import event_stream


class IngestionAgent:
    name = "Ingestion Agent"

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        event_stream.log(self.name, "normalize", {"payload": payload})
        normalized = {
            "ticket_id": payload["ticket_id"],
            "text": payload["text"].strip(),
            "source": payload.get("source", "support"),
            "metadata": payload.get("metadata", {}),
        }
        event_stream.log(self.name, "normalized", normalized)
        return normalized
