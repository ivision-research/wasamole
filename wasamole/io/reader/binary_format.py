from typing import List, Type

from wasamole.util.bytes_reader import ByteReader
from wasamole.core.module import Module
from wasamole.core.elem import Elem
from wasamole.core.function import Function
from wasamole.core.localvar import Local
from wasamole.core.globalvar import Global
from wasamole.core.instructions import disassemble
from wasamole.core.types import (
    ValueType,
    FunctionType,
    TableType,
    ElemType,
    LimitType,
    MutType,
    GlobalType,
    MemoryType,
)
from wasamole.core.exports import (
    BaseExport,
    FuncExport,
    TypeExport,
    MemExport,
    GlobalExport,
)
from wasamole.core.imports import (
    BaseImport,
    TypeImport,
    TableImport,
    MemoryImport,
    GlobalImport,
)


class BinaryReader:
    def __init__(self, bytez: bytes) -> None:
        self.r = ByteReader(bytez)
        self.module = Module()

    @staticmethod
    def from_bytes(bytez: bytes) -> "BinaryReader":
        return BinaryReader(bytez)

    @staticmethod
    def from_file(filename: str) -> "BinaryReader":
        with open(filename, "rb") as f:
            return BinaryReader.from_bytes(f.read())
        return None

    def read(self) -> Module:
        self.r.ensure(b"\x00asm")
        version = self.r.u32()

        while not self.r.eos():
            self._read_section()

        return self.module

    #
    # Sections
    #

    def _read_section(self) -> None:
        section_type = self.r.u8()
        section_size = self.r.uleb()

        type_read_map = {
            0: self._read_custom,
            1: self._read_typesec,
            2: self._read_importsec,
            3: self._read_funcsec,
            4: self._read_tablesec,
            5: self._read_memorysec,
            6: self._read_globalsec,
            7: self._read_exportsec,
            8: self._read_startsec,
            9: self._read_elemsec,
            10: self._read_codesec,
            11: self._read_datasec,
        }

        type_read_map[section_type](section_size)

    def _read_custom(self, size: int) -> None:
        r = ByteReader(self.r.read(size))
        name = r.read(r.uleb()).decode()
        if name == "name":
            while not r.eos():
                section_id = r.u8()
                section_size = r.uleb()
                if section_id == 1:
                    for name_i in range(r.uleb()):
                        function_index = r.uleb()
                        function_name = r.read(r.uleb()).decode()
                        self.module.functions[name_i].set_name(function_name)

    def _read_typesec(self, size: int) -> None:
        for type_i in range(self.r.uleb()):
            self.r.ensure(b"\x60")
            params = self._read_values()
            results = self._read_values()
            self.module.add_type(FunctionType(params, results))

    def _read_importsec(self, size: int) -> None:
        for import_i in range(self.r.uleb()):
            self.module.add_import(self._read_import())

    def _read_funcsec(self, size: int) -> None:
        for func_i in range(self.r.uleb()):
            index = self.r.uleb()
            self.module.add_function(Function(index))

    def _read_tablesec(self, size: int) -> None:
        for table_i in range(self.r.uleb()):
            self.module.add_table(self._read_table_type())

    def _read_memorysec(self, size: int) -> None:
        for memory_i in range(self.r.uleb()):
            self.module.add_memory(self._read_memory_type())

    def _read_globalsec(self, size: int) -> None:
        for global_i in range(self.r.uleb()):
            global_type = self._read_global_type()
            init_expression = disassemble(self.r.read_until(0x0B))
            self.module.add_global(Global(global_type, init_expression))

    def _read_exportsec(self, size: int) -> None:
        for export_i in range(self.r.uleb()):
            self.module.add_export(self._read_export())

    def _read_startsec(self, size: int) -> None:
        self.module.set_start(self.r.uleb())

    def _read_elemsec(self, size: int) -> None:
        for elem_i in range(self.r.uleb()):
            table_index = self.r.uleb()
            offset_expression = disassemble(self.r.read_until(0x0B))
            func_indices = [self.r.uleb() for index_i in range(self.r.uleb())]
            self.module.add_elem(Elem(table_index, offset_expression, func_indices))

    def _read_codesec(self, size: int) -> None:
        for code_i in range(self.r.uleb()):
            function = self.module.functions[code_i]
            code_size = self.r.uleb()
            code_address = self.r.tell()

            # Setup another byte reader to pick aport the code section.
            code_reader = ByteReader(self.r.read(code_size))
            for local_i in range(code_reader.uleb()):
                local_count = code_reader.uleb()
                local_type = code_reader.u8()
                for _ in range(local_count):
                    function.add_local(Local(ValueType(local_type)))

            # The rest of the byte stream is the instructions.
            function.set_name(f"(;{code_i};)")
            function.set_size(code_size - code_reader.tell())
            function.set_address(code_address + code_reader.tell())
            function.append_instructions(disassemble(code_reader.read()))

    def _read_datasec(self, size: int) -> None:
        # TODO: Implement data sections.
        self.r.read(size)

    #
    # Types
    #

    def _read_name(self) -> str:
        return self.r.read(self.r.uleb()).decode()

    def _read_values(self) -> List[ValueType]:
        count = self.r.uleb()
        return list(map(ValueType, [self.r.u8() for i in range(count)]))

    def _read_import(self) -> BaseImport:
        module_name = self._read_name()
        name = self._read_name()
        import_type = self.r.u8()

        if import_type == 0x0:
            index = self.r.uleb()
            return TypeImport(module_name, name, index)
        elif import_type == 0x1:
            return TableImport(module_name, name, self._read_table_type())
        elif import_type == 0x2:
            return MemoryImport(module_name, name, self._read_memory_type())
        elif import_type == 0x3:
            return GlobalImport(module_name, name, self._read_global_type())
        else:
            raise Exception("unexpected import type")

    def _read_export(self) -> BaseExport:
        name = self._read_name()
        export_type = self.r.u8()
        index = self.r.uleb()

        if export_type == 0x0:
            return FuncExport(name, index)
        elif export_type == 0x1:
            return TypeExport(name, index)
        elif export_type == 0x2:
            return MemExport(name, index)
        elif export_type == 0x3:
            return GlobalExport(name, index)
        else:
            raise Exception("unexpected export type")

    def _read_limits(self) -> LimitType:
        limit_type = self.r.u8()
        minimum = self.r.uleb()
        maximum = None
        if limit_type == 0x1:
            maximum = self.r.uleb()
        return LimitType(minimum, maximum)

    def _read_table_type(self) -> TableType:
        elem_type = ElemType(self.r.u8())
        return TableType(elem_type, self._read_limits())

    def _read_memory_type(self) -> MemoryType:
        return MemoryType(self._read_limits())

    def _read_global_type(self) -> GlobalType:
        value_type = ValueType(self.r.u8())
        mut = MutType(self.r.u8())
        return GlobalType(value_type, mut)
