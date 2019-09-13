import dataclasses
from typing import List

from .instructions import Instruction
from .types import GlobalType


@dataclasses.dataclass
class Global:
    type: GlobalType
    init_expression: List[Instruction]
