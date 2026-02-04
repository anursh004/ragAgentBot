from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class MemoryRecord:
    memory_type: str
    content: Dict[str, Any]
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


class MemoryStore:
    def __init__(self) -> None:
        self.working_memory: List[MemoryRecord] = []
        self.episodic_memory: List[MemoryRecord] = []
        self.semantic_memory: List[MemoryRecord] = []

    def write(self, memory_type: str, content: Dict[str, Any]) -> MemoryRecord:
        record = MemoryRecord(memory_type=memory_type, content=content)
        if memory_type == "working":
            self.working_memory.append(record)
        elif memory_type == "episodic":
            self.episodic_memory.append(record)
        elif memory_type == "semantic":
            self.semantic_memory.append(record)
        return record

    def read(self, memory_type: str) -> List[MemoryRecord]:
        if memory_type == "working":
            return list(self.working_memory)
        if memory_type == "episodic":
            return list(self.episodic_memory)
        if memory_type == "semantic":
            return list(self.semantic_memory)
        return []


memory_store = MemoryStore()
