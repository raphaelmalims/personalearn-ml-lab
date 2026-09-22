"""Minimal scalar Value for Tue: build the computation graph.

Wed TODO: _backward closures, topological sort, and Value.backward().
"""

from __future__ import annotations

from typing import Optional, Set, Union


class Value:
    def __init__(
        self,
        data: float,
        _children: tuple["Value", ...] = (),
        _op: str = "",
        label: str = "",
    ) -> None:
        self.data = float(data)
        self.grad = 0.0
        self._prev: Set["Value"] = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self) -> str:
        name = self.label or f"{self.data}"
        return f"Value(data={self.data}, label={name!r}, op={self._op!r})"

    def __add__(self, other: Union["Value", float]) -> "Value":
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other: Union["Value", float]) -> "Value":
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data * other.data, (self, other), "*")

    # Wed: def backward(self) -> None: ...
