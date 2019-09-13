import dataclasses
from enum import Enum
from typing import List, Dict, Optional


class ValueType(Enum):
    i32 = 0x7F
    i64 = 0x7E
    f32 = 0x7D
    f64 = 0x7C


class ElemType(Enum):
    funcref = 0x70


class MutType(Enum):
    const = 0x0
    var = 0x1


@dataclasses.dataclass
class FunctionType:
    params: List[ValueType]
    results: List[ValueType]


@dataclasses.dataclass
class LimitType:
    minimum: int
    maximum: Optional[int]


@dataclasses.dataclass
class TableType:
    elemtype: ElemType
    limits: LimitType


@dataclasses.dataclass
class MemoryType:
    limits: LimitType


@dataclasses.dataclass
class GlobalType:
    valtype: ValueType
    mut: MutType
