from dataclasses import dataclass

@dataclass
class Rule:
    min_alive_count: int
    max_alive_count: int
    alive: bool
    action: str
    description: str
