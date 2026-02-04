from typing import Any, Dict

from app.observability import event_stream


class IntentClassificationAgent:
    name = "Intent & Classification Agent"

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        text = payload["text"].lower()
        urgency = "low"
        intent = "general"
        if "failing" in text or "incident" in text:
            urgency = "high"
            intent = "incident"
        event_stream.log(self.name, "classified", {"intent": intent, "urgency": urgency})
        return {"intent": intent, "urgency": urgency, "sla_risk": urgency == "high"}
