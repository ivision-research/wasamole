from typing import Any, List

from wasamole.core.exports import BaseExport, FuncExport
from wasamole.core.module import Module
from wasamole.core.function import Function
from wasamole.core.instructions import Opcode
from wasamole.core.imports import BaseImport, TypeImport
from wasamole.core.types import FunctionType, GlobalType, MemoryType, TableType


class TextWriter:
    class Indent:
        def __init__(self, tw: "TextWriter") -> None:
            self.tw = tw

        def __enter__(self) -> "TextWriter.Indent":
            self.tw.indent += 2
            return self

        def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
            self.tw.indent -= 2

    def __init__(self, module: Module) -> None:
        self.module: Module = module
        self.buffer: List[str] = []
        self.indent: int = 0

    def write(self) -> str:
        self._writeln("(module")

        # Write out types.
        with TextWriter.Indent(self):
            for i, type in enumerate(self.module.types):
                self._write(f"(type (;{i};) ")
                self._write_function_type(type)
                self._writeln(")")

        # Write out imports.
        with TextWriter.Indent(self):
            for i, imp in enumerate(self.module.imports):
                imp = self.module.imports[i]
                self._write(f'(import "{imp.module_name}" "{imp.name}" ')
                self._write_import(i, imp)
                self._writeln(")")

        # Write out code sections.
        with TextWriter.Indent(self):
            for i, function in enumerate(self.module.functions):
                self._write(f"(func {function.name} (type {function.type_index})")
                self._write_function(function)
                self._writeln(")")

        # Write out memory sections.
        with TextWriter.Indent(self):
            for i, memory in enumerate(self.module.memories):
                self._write(f"(memory (;{i};) {memory.limits.minimum}")
                if memory.limits.maximum:
                    self._write(f"{memory.limits.maximum}")
                self._writeln(")")

        # Write out export sections.
        with TextWriter.Indent(self):
            for i, export in enumerate(self.module.exports):
                export = self.module.exports[i]
                self._write(f'(export "{export.name}" ')
                self._write_export(i, export)
                self._writeln(")")

        self._writeln(")")
        return "".join(self.buffer)

    def _write(self, s: str) -> "TextWriter":
        if len(self.buffer) and len(self.buffer[-1]) and self.buffer[-1][-1] == "\n":
            self._indent()
        self.buffer.append(s)
        return self

    def _nl(self) -> "TextWriter":
        self._write("\n")
        return self

    def _writeln(self, s: str) -> "TextWriter":
        return self._write(s)._nl()

    def _indent(self) -> "TextWriter":
        self.buffer.append(" " * self.indent)
        return self

    def _write_function_type(self, ft: FunctionType) -> None:
        self._write("(func")
        if len(ft.params):
            self._write(" (param " + " ".join(map(lambda p: p.name, ft.params)) + ")")
        if len(ft.results):
            self._write(" (result " + " ".join(map(lambda r: r.name, ft.results)) + ")")
        self._write(")")

    def _write_import(self, i: int, bi: BaseImport) -> None:
        if isinstance(bi, TypeImport):
            self._write(f"(func (;{i};) (type {bi.index}))")

    def _write_function(self, f: Function) -> None:
        with TextWriter.Indent(self):
            self._nl()
            if len(f.locals):
                self._write("(local ")
                self._write(" ".join([str(l.type.name) for l in f.locals]))
                self._writeln(")")
            for i, instr in enumerate(f.instructions, start=1):
                if instr.opcode == Opcode.END and (i == len(f.instructions)):
                    break
                if instr.ends_block():
                    self.indent -= 2
                self._writeln(str(instr))
                if instr.starts_block():
                    self.indent += 2

    def _write_export(self, i: int, be: BaseExport) -> None:
        if isinstance(be, FuncExport):
            self._write(f"(func {be.index})")
