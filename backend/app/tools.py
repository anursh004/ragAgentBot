from typing import Any, Callable, Dict

from app.observability import event_stream


def run_tool(agent: str, name: str, payload: Dict[str, Any], func: Callable[..., Any]) -> Any:
    event_stream.log(agent, f"tool:{name}:input", payload)
    result = func(**payload)
    event_stream.log(agent, f"tool:{name}:output", {"result": result})
    return result
