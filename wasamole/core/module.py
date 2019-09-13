from .elem import Elem
from .exports import BaseExport
from .function import Function
from .globalvar import Global
from .imports import BaseImport
from .types import FunctionType, GlobalType, MemoryType, TableType

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Module:
    types: List[FunctionType] = field(default_factory=list)
    imports: List[BaseImport] = field(default_factory=list)
    functions: List[Function] = field(default_factory=list)
    tables: List[TableType] = field(default_factory=list)
    memories: List[MemoryType] = field(default_factory=list)
    globals: List[Global] = field(default_factory=list)
    exports: List[BaseExport] = field(default_factory=list)
    start: Optional[int] = None
    elems: List[Elem] = field(default_factory=list)

    def type_at(self, i: int) -> FunctionType:
        return self.types[i]

    def add_type(self, ft: FunctionType) -> None:
        self.types.append(ft)

    def add_import(self, bi: BaseImport) -> None:
        self.imports.append(bi)

    def add_function(self, f: Function) -> None:
        self.functions.append(f)

    def add_table(self, t: TableType) -> None:
        self.tables.append(t)

    def add_memory(self, m: MemoryType) -> None:
        self.memories.append(m)

    def add_global(self, g: Global) -> None:
        self.globals.append(g)

    def add_export(self, e: BaseExport) -> None:
        self.exports.append(e)

    def set_start(self, s: int) -> None:
        self.start = s

    def add_elem(self, e: Elem) -> None:
        self.elems.append(e)
