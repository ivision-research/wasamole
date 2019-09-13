import dataclasses


@dataclasses.dataclass
class BaseExport:
    name: str
    index: int


class FuncExport(BaseExport):
    pass


class TypeExport(BaseExport):
    pass


class MemExport(BaseExport):
    pass


class GlobalExport(BaseExport):
    pass
