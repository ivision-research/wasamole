from dataclasses import dataclass, field
from enum import Enum
from typing import List, Type, Union, Optional

from .types import ValueType
from wasamole.util.bytes_reader import ByteReader

# Instructions
#
# https://webassembly.github.io/spec/core/binary/instructions.html
#
class Opcode(Enum):
    # Control Instructions
    #
    # https://webassembly.github.io/spec/core/binary/instructions.html#control-instructions
    #
    UNREACHABLE = 0x00
    NOP = 0x01
    BLOCK = 0x02
    LOOP = 0x03
    IF = 0x04
    ELSE = 0x05
    END = 0x0B
    BR = 0x0C
    BR_IF = 0x0D
    BR_TABLE = 0x0E
    RETURN = 0x0F
    CALL = 0x10
    CALL_INDIRECT = 0x11

    # Parametric Instructions:
    #
    # https://webassembly.github.io/spec/core/binary/instructions.html#parametric-instructions
    #
    DROP = 0x1A
    SELECT = 0x1B

    # Variable Instructions:
    #
    # https://webassembly.github.io/spec/core/binary/instructions.html#variable-instructions
    #
    LOCAL_GET = 0x20
    LOCAL_SET = 0x21
    LOCAL_TEE = 0x22
    GLOBAL_GET = 0x23
    GLOBAL_SET = 0x24

    # Memory Instrutions:
    #
    # https://webassembly.github.io/spec/core/binary/instructions.html#memory-instructions
    #

    # Loads
    I32_LOAD = 0x28
    I64_LOAD = 0x29
    F32_LOAD = 0x2A
    F64_LOAD = 0x2B
    I32_LOAD8_S = 0x2C
    I32_LOAD8_U = 0x2D
    I32_LOAD16_S = 0x2E
    I32_LOAD16_U = 0x2F
    I64_LOAD8_S = 0x30
    I64_LOAD8_U = 0x31
    I64_LOAD16_S = 0x32
    I64_LOAD16_U = 0x33
    I64_LOAD32_S = 0x34
    I64_LOAD32_U = 0x35

    # Stores
    I32_STORE = 0x36
    I64_STORE = 0x37
    F32_STORE = 0x38
    F64_STORE = 0x39
    I32_STORE8 = 0x3A
    I32_STORE16 = 0x3B
    I64_STORE8 = 0x3C
    I64_STORE16 = 0x3D
    I64_STORE32 = 0x3E
    MEMORY_SIZE = 0x3F
    MEMORY_GROW = 0x40

    # Numeric Instructions:
    #
    # https://webassembly.github.io/spec/core/binary/instructions.html#numeric-instructions
    #

    # Constant Loads
    I32_CONST = 0x41
    I64_CONST = 0x42
    F32_CONST = 0x43
    F64_CONST = 0x44

    # i32 Comparisons
    I32_EQZ = 0x45
    I32_EQ = 0x46
    I32_NE = 0x47
    I32_LT_S = 0x48
    I32_LT_U = 0x49
    I32_GT_S = 0x4A
    I32_GT_U = 0x4B
    I32_LE_S = 0x4C
    I32_LE_U = 0x4D
    I32_GE_S = 0x4E
    I32_GE_U = 0x4F

    # i64 Comparisons
    I64_EQZ = 0x50
    I64_EQ = 0x51
    I64_NE = 0x52
    I64_LT_S = 0x53
    I64_LT_U = 0x54
    I64_GT_S = 0x55
    I64_GT_U = 0x56
    I64_LE_S = 0x57
    I64_LE_U = 0x58
    I64_GE_S = 0x59
    I64_GE_U = 0x5A

    # f32 Comparisons
    F32_EQ = 0x5B
    F32_NE = 0x5C
    F32_LT = 0x5D
    F32_GT = 0x5E
    F32_LE = 0x5F
    F32_GE = 0x60

    # f64 Comparisons
    F64_EQ = 0x61
    F64_NE = 0x62
    F64_LT = 0x63
    F64_GT = 0x64
    F64_LE = 0x65
    F64_GE = 0x66

    # i32 Arithmetic
    I32_CLZ = 0x67
    I32_CTZ = 0x68
    I32_POPCNT = 0x69
    I32_ADD = 0x6A
    I32_SUB = 0x6B
    I32_MUL = 0x6C
    I32_DIV_S = 0x6D
    I32_DIV_U = 0x6E
    I32_REM_S = 0x6F
    I32_REM_U = 0x70
    I32_AND = 0x71
    I32_OR = 0x72
    I32_XOR = 0x73
    I32_SHL = 0x74
    I32_SHR_S = 0x75
    I32_SHR_U = 0x76
    I32_ROTL = 0x77
    I32_ROTR = 0x78

    # i64 Arithmetic
    I64_CLZ = 0x79
    I64_CTZ = 0x7A
    I64_POPCNT = 0x7B
    I64_ADD = 0x7C
    I64_SUB = 0x7D
    I64_MUL = 0x7E
    I64_DIV_S = 0x7F
    I64_DIV_U = 0x80
    I64_REM_S = 0x81
    I64_REM_U = 0x82
    I64_AND = 0x83
    I64_OR = 0x84
    I64_XOR = 0x85
    I64_SHL = 0x86
    I64_SHR_S = 0x87
    I64_SHR_U = 0x88
    I64_ROTL = 0x89
    I64_ROTR = 0x8A

    # f32 Arithmetic
    F32_ABS = 0x8B
    F32_NEG = 0x8C
    F32_CEIL = 0x8D
    F32_FLOOR = 0x8E
    F32_TRUNC = 0x8F
    F32_NEAREST = 0x90
    F32_SQRT = 0x91
    F32_ADD = 0x92
    F32_SUB = 0x93
    F32_MUL = 0x94
    F32_DIV = 0x95
    F32_MIN = 0x96
    F32_MAX = 0x97
    F32_COPYSIGN = 0x98

    # f64 Arithmetic
    F64_ABS = 0x99
    F64_NEG = 0x9A
    F64_CEIL = 0x9B
    F64_FLOOR = 0x9C
    F64_TRUNC = 0x9D
    F64_NEAREST = 0x9E
    F64_SQRT = 0x9F
    F64_ADD = 0xA0
    F64_SUB = 0xA1
    F64_MUL = 0xA2
    F64_DIV = 0xA3
    F64_MIN = 0xA4
    F64_MAX = 0xA5
    F64_COPYSIGN = 0xA6

    # Conversions
    I32_WRAP_I64 = 0xA7
    I32_TRUNC_F32_S = 0xA8
    I32_TRUNC_F32_U = 0xA9
    I32_TRUNC_F64_S = 0xAA
    I32_TRUNC_F64_U = 0xAB
    I64_EXTEND_I32_S = 0xAC
    I64_EXTEND_I32_U = 0xAD
    I64_TRUNC_F32_S = 0xAE
    I64_TRUNC_F32_U = 0xAF
    I64_TRUNC_F64_S = 0xB0
    I64_TRUNC_F64_U = 0xB1
    F32_CONVERT_I32_S = 0xB2
    F32_CONVERT_I32_U = 0xB3
    F32_CONVERT_I64_S = 0xB4
    F32_CONVERT_I64_U = 0xB5
    F32_DEMOTE_F64 = 0xB6
    F64_CONVERT_I32_S = 0xB7
    F64_CONVERT_I32_U = 0xB8
    F64_CONVERT_I64_S = 0xB9
    F64_CONVERT_I64_U = 0xBA
    F64_PROMOTE_F32 = 0xBB
    I32_REINTERPRET_F32 = 0xBC
    I64_REINTERPRET_F64 = 0xBD
    F32_REINTERPRET_I32 = 0xBE
    F64_REINTERPRET_I64 = 0xBF


@dataclass
class Operand(object):
    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return str(self)


@dataclass
class BlockTypeOperand(Operand):
    result_type: Optional[ValueType] = None

    def __str__(self) -> str:
        if self.result_type:
            return f"(result {self.result_type.name})"
        return ""

    def __repr__(self) -> str:
        return str(self)


@dataclass
class MemArgOperand(Operand):
    align: int
    offset: int

    def __str__(self) -> str:
        me = []
        if self.offset:
            me.append(f"offset={self.offset}")
        if self.align:
            me.append(f"align={self.align}")
        return " ".join(me)


@dataclass
class IndexOperand(Operand):
    index: int

    def __str__(self) -> str:
        return str(self.index)


@dataclass
class IndexVectorOperand(Operand):
    indices: List[int] = field(default_factory=list)

    def __str__(self) -> str:
        return "[{0}]".format(", ".join(map(str, self.indices)))

    def append_index(self, index: int) -> None:
        self.indices.append(index)


class ZeroOperand(Operand):
    def __str__(self) -> str:
        return "0x0"


@dataclass
class NumericOperand(Operand):
    width: int = 0
    value: Union[int, float] = 0

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)


class I32Operand(NumericOperand):
    def __init__(self, value: int) -> None:
        super().__init__(4, value)


class I64Operand(NumericOperand):
    def __init__(self, value: int) -> None:
        super().__init__(8, value)


@dataclass
class F32Operand(NumericOperand):
    def __init__(self, value: float) -> None:
        super().__init__(4, value)


class F64Operand(NumericOperand):
    def __init__(self, value: float) -> None:
        super().__init__(8, value)


@dataclass
class Instruction:
    opcode: Opcode
    operands: List[Operand] = field(default_factory=list)
    size: int = 0

    def __post_init__(self) -> None:
        self.operands = [Operand()] * len(self.operand_types)

    @property
    def opname(self) -> str:
        return self.opcode.name.lower().replace("_", ".", 1)

    @property
    def operand_types(self) -> List[Type[Operand]]:
        opcode = self.opcode.value
        if opcode in [Opcode.BLOCK.value, Opcode.LOOP.value, Opcode.IF.value]:
            return [BlockTypeOperand]
        elif opcode >= Opcode.LOCAL_GET.value and opcode <= Opcode.GLOBAL_SET.value:
            return [IndexOperand]
        elif opcode == Opcode.CALL_INDIRECT.value:
            return [IndexOperand, ZeroOperand]
        elif opcode in [Opcode.BR.value, Opcode.BR_IF.value, Opcode.CALL.value]:
            return [IndexOperand]
        elif opcode in [Opcode.BR_TABLE.value]:
            return [IndexVectorOperand, IndexOperand]
        elif opcode >= Opcode.I32_LOAD.value and opcode <= Opcode.I64_STORE32.value:
            return [MemArgOperand]
        elif opcode in [Opcode.MEMORY_SIZE.value, Opcode.MEMORY_GROW.value]:
            return [ZeroOperand]
        elif opcode == Opcode.I32_CONST.value:
            return [I32Operand]
        elif opcode == Opcode.I64_CONST.value:
            return [I64Operand]
        elif opcode == Opcode.F32_CONST.value:
            return [F32Operand]
        elif opcode == Opcode.F64_CONST.value:
            return [F64Operand]

        return []

    def set_operand(self, index: int, operand: Operand) -> None:
        self.operands[index] = operand

    def set_size(self, size: int) -> None:
        self.size = size

    def starts_block(self) -> bool:
        return self.opcode in [Opcode.BLOCK, Opcode.LOOP, Opcode.IF, Opcode.ELSE]

    def ends_block(self) -> bool:
        return self.opcode in [Opcode.ELSE, Opcode.END]

    def __str__(self) -> str:
        me = self.opname
        for i in range(0, len(self.operands)):
            if i > 1:
                me += ","
            operand_str = str(self.operands[i])
            if len(operand_str):
                me += " " + operand_str
        return me

    def __repr__(self) -> str:
        return str(self)


def disassemble_instruction(data: bytes) -> Instruction:
    r = ByteReader(data)
    instr = Instruction(Opcode(r.u8()))

    for i in range(0, len(instr.operand_types)):
        operand = instr.operand_types[i]
        size = 1
        if operand == ZeroOperand:
            instr.set_operand(i, ZeroOperand())
        elif operand == IndexOperand:
            instr.set_operand(i, IndexOperand(r.uleb()))
        elif operand == IndexVectorOperand:
            ivo = IndexVectorOperand()
            for label_i in range(r.uleb()):
                ivo.append_index(r.uleb())
            instr.set_operand(i, ivo)
        elif operand == BlockTypeOperand:
            result_type = r.uleb()
            if result_type != 0x40:
                instr.set_operand(i, BlockTypeOperand(ValueType(result_type)))
            else:
                instr.set_operand(i, BlockTypeOperand())
        elif operand == MemArgOperand:
            instr.set_operand(i, MemArgOperand(r.uleb(), r.uleb()))
        elif operand == I32Operand:
            instr.set_operand(i, I32Operand(r.sleb()))
        elif operand == I64Operand:
            instr.set_operand(i, I64Operand(r.sleb()))
        elif operand == F32Operand:
            instr.set_operand(i, F32Operand(r.f32()))
        elif operand == F64Operand:
            instr.set_operand(i, F64Operand(r.f64()))

    instr.set_size(r.tell())
    return instr


def disassemble(data: bytes) -> List[Instruction]:
    offset = 0
    instrs = []

    while offset < len(data):
        instr = disassemble_instruction(data[offset:])
        instrs.append(instr)
        offset += instr.size

    return instrs
