# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, ElemType, MutType

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_memories():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "memories.wasm")
    assert len(wasm_binary.memories) == 1


def test_tables_type():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "memories.wasm")
    memory = wasm_binary.memories[0]
    assert memory.limits.minimum == 0
    assert memory.limits.maximum == 65536
