# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, ElemType, MutType

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_start():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "start.wasm")
    assert wasm_binary.start == 2


def test_no_start():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "globals.wasm")
    assert wasm_binary.start == None
