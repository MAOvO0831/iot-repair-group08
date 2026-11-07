from enum import Enum

class Status(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"


def can_transition(current: Status, target: Status) -> bool:
    if current == Status.PENDING and target == Status.PROCESSING:
        return True
    if current == Status.PROCESSING and target == Status.COMPLETED:
        return True
    return False

