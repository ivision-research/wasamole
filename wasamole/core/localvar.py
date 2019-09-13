import dataclasses

from .types import ValueType


@dataclasses.dataclass
class Local:
    type: ValueType
