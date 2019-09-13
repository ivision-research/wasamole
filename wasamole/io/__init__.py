from wasamole.core.module import Module

from .reader.binary_format import BinaryReader

from .writer.text_format import TextWriter


def from_bytes(the_bytes: bytes) -> Module:
    return BinaryReader.from_bytes(the_bytes).read()


def from_file(filename: str) -> Module:
    return BinaryReader.from_file(filename).read()


def to_text_string(module: Module) -> str:
    return TextWriter(module).write()
