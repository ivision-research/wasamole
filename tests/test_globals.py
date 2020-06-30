# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, ElemType, MutType

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_globals():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "globals.wasm")
    assert len(wasm_binary.globals) == 9


def test_tables_type():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "globals.wasm")

    globl = wasm_binary.globals[0]
    assert len(globl.init_expression) == 2
    assert str(globl.init_expression[0]) == "i32.const -2"

    globl = wasm_binary.globals[-1]
    assert len(globl.init_expression) == 2
    assert str(globl.init_expression[0]) == "global.get 0"
