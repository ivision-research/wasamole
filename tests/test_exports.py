# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, ElemType, MutType

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_imports():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "exports.wasm")
    assert len(wasm_binary.exports) == 6


def test_function_imports():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "exports.wasm")
    for i in range(0, 6):
        imp = wasm_binary.exports[i]
        assert imp.name == "{0}".format(chr(ord("a") + i))
        assert imp.index == 0
