from .instructions import Instruction
from .types import FunctionType, GlobalType, MemoryType, TableType, ValueType
from .localvar import Local

from dataclasses import dataclass, field
from typing import List


@dataclass
class Function:
    type_index: int
    locals: List[Local] = field(default_factory=list)
    instructions: List[Instruction] = field(default_factory=list)
    size: int = 0
    address: int = 0
    name: str = ""

    def add_local(self, local: Local) -> None:
        self.locals.append(local)

    def append_instructions(self, instrs: List[Instruction]) -> None:
        self.instructions += instrs

    def set_size(self, size: int) -> None:
        self.size = size

    def set_address(self, addr: int) -> None:
        self.address = addr

    def set_name(self, name: str) -> None:
        self.name = name
