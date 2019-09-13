# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, ElemType, MutType

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_elems():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "elems.wasm")
    assert len(wasm_binary.elems) == 12


def test_elems_offsets():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "exports.wasm")

    for elem in wasm_binary.elems:
        assert len(elem.offset_expression) == 1
        assert str(elem.offset_expression[0]) == "i32_const 0"


def test_elems_indices():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "exports.wasm")

    expected = [[], [0, 0]]
    for i in range(0, len(wasm_binary.elems)):
        elem = wasm_binary.elems[i]
        assert elem.function_indices == expected[i % 2]
