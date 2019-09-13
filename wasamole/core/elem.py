from .instructions import Instruction

from dataclasses import dataclass
from typing import List


@dataclass
class Elem:
    table_index: int
    offset_expression: List[Instruction]
    function_indices: List[int]
