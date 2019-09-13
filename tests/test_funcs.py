# -*- coding: utf-8 -*-

from pathlib import Path
from .context import wasamole
from wasamole.core import ValueType, Function

TEST_DATA_DIR = Path(__file__).resolve().parent / "data"


def test_func0():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "funcs.wasm")
    ft = wasm_binary.types[wasm_binary.functions[0].type_index]
    assert len(ft.params) == 0
    assert ft.results[0] == ValueType.i32


def test_func1():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "funcs.wasm")
    ft = wasm_binary.types[wasm_binary.functions[1].type_index]
    assert len(ft.params) == 0
    assert ft.results[0] == ValueType.i64


def test_func2():
    wasm_binary = wasamole.io.from_file(TEST_DATA_DIR / "funcs.wasm")
    ft = wasm_binary.types[wasm_binary.functions[2].type_index]
    params = ft.params
    results = ft.results
    assert len(params) == 4
    assert params[0] == ValueType.i32
    assert params[1] == ValueType.f32
    assert params[2] == ValueType.i64
    assert params[3] == ValueType.f64
    assert len(results) == 1
    assert results[0] == ValueType.i64
