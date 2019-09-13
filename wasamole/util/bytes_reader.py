import struct
from typing import List, cast


class ByteReader(object):
    def __init__(self, data: bytes) -> None:
        self.offset: int = 0
        self.data: bytes = data

    def peek(self, count: int) -> bytes:
        return self.data[self.offset : self.offset + count]

    def read(self, count: int = 0) -> bytes:
        if not count:
            count = len(self.data) - self.offset
        bytez = self.peek(count)
        self.offset += count
        return bytez

    def read_until(self, byte: int) -> bytes:
        bytez = b""
        while ord(self.peek(1)) != byte:
            bytez += self.read(1)
        return bytez + self.read(1)

    def u8(self) -> int:
        return cast(int, struct.unpack(b"B", self.read(1))[0])

    def u16(self) -> int:
        return cast(int, struct.unpack(b"H", self.read(2))[0])

    def u32(self) -> int:
        return cast(int, struct.unpack(b"I", self.read(4))[0])

    def f32(self) -> float:
        return cast(float, struct.unpack(b"<f", self.read(4))[0])

    def f64(self) -> float:
        return cast(float, struct.unpack(b"<d", self.read(8))[0])

    def uleb(self) -> int:
        result = shift = 0
        while True:
            byte = ord(self.read(1))
            result |= (byte & 0x7F) << shift
            shift += 7
            if (byte & 0x80) == 0:
                break
        return result

    def sleb(self) -> int:
        result = shift = 0
        while True:
            byte = ord(self.read(1))
            result |= (byte & 0x7F) << shift
            shift += 7
            if (byte & 0x80) == 0:
                break
        if result & 0x40:
            result |= ~0 << shift
        return result

    def ensure(self, b: bytes) -> None:
        assert self.read(len(b)) == b

    def eos(self) -> bool:
        return self.offset >= len(self.data)

    def tell(self) -> int:
        return self.offset
