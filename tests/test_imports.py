# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, ElemType, MutType

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_imports():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "imports.wasm")
    assert len(wasm_binary.imports) == 13


def test_function_imports():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "imports.wasm")
    for i in range(0, 7):
        imp = wasm_binary.imports[i]
        assert imp.module_name == "test"
        assert imp.name == "func{0}".format(i)
        assert imp.index == i


def test_memory_imports():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "imports.wasm")
    imp = wasm_binary.imports[8]
    assert imp.module_name == "test"
    assert imp.name == "memory"
    assert imp.memory_type.limits.minimum == 1
    assert imp.memory_type.limits.maximum == 2


def test_table_imports():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "imports.wasm")
    imp = wasm_binary.imports[7]
    assert imp.module_name == "test"
    assert imp.name == "table"
    assert imp.table_type.elemtype == ElemType.funcref
    assert imp.table_type.limits.minimum == 10
    assert imp.table_type.limits.maximum == 20


def test_global_imports():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "imports.wasm")
    for i in range(9, 13):
        imp = wasm_binary.imports[i]
        assert imp.module_name == "test"
        assert imp.name == "global{0}".format(i - 9)
        assert imp.global_type.valtype == ValueType(0x7F - (i - 9))
        assert imp.global_type.mut == MutType.const
