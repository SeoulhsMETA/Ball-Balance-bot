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
        return self._data[self._pointer]

    @property
    def pointer(self) -> int:
        """get pointer"""
        return self._pointer

    @pointer.setter
    def pointer(self, new: int) -> None:
        """set pointer"""
        self._pointer = new % len(self._data)

    def __init__(self, data: Sequence[T]) -> None:
        super().__init__()
        self._pointer = 0
        self._data = tuple(data)

    def __next__(self) -> T:
        self.pointer += 1
        return self._data[self._pointer - 1]
