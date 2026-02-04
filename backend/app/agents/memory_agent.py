from typing import Any, Dict, List

from app.memory_store import memory_store
from app.observability import event_stream
from app.tools import run_tool


def write_memory(memory_type: str, content: Dict[str, Any]) -> Dict[str, Any]:
    record = memory_store.write(memory_type, content)
    return {"memory_type": record.memory_type, "timestamp": record.timestamp}


def read_memory(memory_type: str) -> List[Dict[str, Any]]:
    return [
        {"memory_type": record.memory_type, "content": record.content, "timestamp": record.timestamp}
        for record in memory_store.read(memory_type)
    ]


class MemoryAgent:
    name = "Memory Agent"

    def read(self, memory_type: str) -> List[Dict[str, Any]]:
        event_stream.log(self.name, "memory:read", {"type": memory_type})
        return run_tool(self.name, "read_memory", {"memory_type": memory_type}, read_memory)

    def write(self, memory_type: str, content: Dict[str, Any]) -> Dict[str, Any]:
        event_stream.log(self.name, "memory:write", {"type": memory_type, "content": content})
        return run_tool(self.name, "write_memory", {"memory_type": memory_type, "content": content}, write_memory)
