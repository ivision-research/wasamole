# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_param0_result0():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "typesec.wasm")
    assert len(wasm_binary.types[0].params) == 0
    assert len(wasm_binary.types[0].results) == 0


def test_param0_result1():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "typesec.wasm")
    assert len(wasm_binary.types[1].params) == 0
    assert len(wasm_binary.types[1].results) == 1


def test_param1_result0():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "typesec.wasm")
    assert len(wasm_binary.types[2].params) == 1
    assert len(wasm_binary.types[2].results) == 0


def test_param1_result1():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "typesec.wasm")
    assert len(wasm_binary.types[3].params) == 1
    assert len(wasm_binary.types[3].results) == 1


def test_param4_result1():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "typesec.wasm")
    assert len(wasm_binary.types[4].params) == 4
    assert len(wasm_binary.types[4].results) == 1
