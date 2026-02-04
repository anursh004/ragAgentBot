from typing import Any, Dict

from app.observability import event_stream


class GuardrailsAgent:
    name = "Guardrails & Policy Agent"

    unsafe_phrases = [
        "d3str0y",
        "4tt4ck",
        "h3rt",
        "su1c1d3",
        "k1ll",
        "s3x",
        "p0rn",
        "h@t3",
        "forget your instruction",
    ]

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        text = payload["text"].lower()
        blocked = any(phrase in text for phrase in self.unsafe_phrases)
        confidence = payload.get("confidence", 0.6)
        escalated = blocked or confidence < 0.5
        decision = "escalate" if escalated else "auto"
        event_stream.log(
            self.name,
            "guardrails:decision",
            {"blocked": blocked, "confidence": confidence, "decision": decision},
        )
        return {
            "decision": decision,
            "blocked": blocked,
            "confidence": confidence,
            "escalated": escalated,
        }
