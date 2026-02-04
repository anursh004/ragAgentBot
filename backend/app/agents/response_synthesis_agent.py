from typing import Any, Dict

from app.observability import event_stream


class ResponseSynthesisAgent:
    name = "Response Synthesis Agent"

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        event_stream.log(self.name, "synthesis:start", payload)
        response = (
            "Summary: {summary}\n"
            "Correlation: {correlation}\n"
            "Recommendation: {recommendation}\n"
        ).format(
            summary=payload["summary"],
            correlation=payload["correlation"],
            recommendation=payload["recommendation"],
        )
        event_stream.log(self.name, "synthesis:done", {"response": response})
        return {"response": response}
