"""Cycled List data structure"""

from __future__ import annotations
from typing import TypeVar
from collections.abc import Iterator, Sequence

T = TypeVar("T")


class CycledList(list[T]):
    """Cycled list"""

    def __iter__(self) -> CycledListIterator:
        return CycledListIterator(self)


class CycledListIterator(Iterator[T]):
    """Iterator for CycledList"""

    @property
    def current(self) -> T:
        """get current indexed data"""
        return self._data[self._index]

    def init(self) -> None:
        """init Iterator, set index 0"""
        self._index = 0

    def __init__(self, data: Sequence[T]) -> None:
        super().__init__()
        self._index = 0
        self._data = tuple(data)

    def __next__(self) -> T:
        self._index = (self._index + 1) % len(self._data)
        return self._data[self._index - 1]
