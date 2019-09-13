from .types import FunctionType, GlobalType, MemoryType, TableType

import dataclasses
from typing import List


@dataclasses.dataclass
class BaseImport:
    module_name: str
    name: str


@dataclasses.dataclass
class TypeImport(BaseImport):
    index: int


@dataclasses.dataclass
class TableImport(BaseImport):
    table_type: TableType


@dataclasses.dataclass
class MemoryImport(BaseImport):
    memory_type: MemoryType


@dataclasses.dataclass
class GlobalImport(BaseImport):
    global_type: GlobalType
