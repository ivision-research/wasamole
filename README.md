# Wasamole

_A tasty framework for WebAssembly Software Analysis_

## Description

Wasamole is a framework for analysing [WebAssembly](https://webassembly.github.io/spec/core/) programs. It is meant to provide:

1. A WASM disassembler.
2. A WASM assembler.
3. A WASM VM implementation.
4. A set of core modules to be used to build other WASM-based tools.

## Development

When working on Wasamole please keep the following things in mind.

### Formatting

All code should be formatted with [black](https://github.com/psf/black). There is a `make` target for it:

`make format`

### Type Checking

All code should be type checked with [mypy](http://mypy-lang.org/).  There is a `make` target for it:

`make typecheck`

### Testing

Run unit tests with:

`make test`
