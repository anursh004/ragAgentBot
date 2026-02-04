from collections import deque
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Deque, Dict, List


@dataclass
class Event:
    timestamp: str
    agent: str
    step: str
    payload: Dict[str, Any]


class EventStream:
    def __init__(self, limit: int = 500) -> None:
        self._events: Deque[Event] = deque(maxlen=limit)

    def log(self, agent: str, step: str, payload: Dict[str, Any]) -> None:
        event = Event(
            timestamp=datetime.utcnow().isoformat(),
            agent=agent,
            step=step,
            payload=payload,
        )
        self._events.append(event)

    def all_events(self) -> List[Event]:
        return list(self._events)


event_stream = EventStream()
