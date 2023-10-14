"""Cycled List data structure"""

from __future__ import annotations
from typing import Any
from collections.abc import Iterator, Sequence


class CycledList(list):
    """Cycled list"""

    def __iter__(self) -> CycledListIterator:
        return CycledListIterator(self)


class CycledListIterator(Iterator):
    """Iterator for CycledList"""

    @property
    def current(self) -> Any:
        """get current indexed data"""
        return self._data[self._index]

    def __init__(self, data: Sequence[Any]) -> None:
        super().__init__()
        self._index = 0
        self._data = tuple(data)

    def __next__(self) -> Any:
        self._index = (self._index + 1) % len(self._data)
        return self._data[self._index - 1]
