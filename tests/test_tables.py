# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, ElemType, MutType

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_tables():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "tables.wasm")
    assert len(wasm_binary.tables) == 1


def test_tables_type():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "tables.wasm")
    table = wasm_binary.tables[0]
    assert table.elemtype == ElemType.funcref
    assert table.limits.minimum == 1
    assert table.limits.maximum == None
