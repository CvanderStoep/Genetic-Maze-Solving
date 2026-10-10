"""Defines a 2D vector type used for positions and movement math. It supports arithmetic operations such as addition, subtraction, scaling, magnitude, and distance calculations."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Vector2D:
    x: float
    y: float

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def dot(self, that: Vector2D) -> float:
        return self.x * that.x + self.y * that.y

    def magnitude(self) -> float:
        # Note: as in the Java original this is the *squared* length.
        return self.dot(self)

    def distance_to(self, that: Vector2D) -> float:
        # Squared distance (the Java original never takes the square root).
        # This preserves the ranking of individuals.
        return self.minus(that).magnitude()

    def scale(self, factor: float) -> Vector2D:
        return Vector2D(factor * self.x, factor * self.y)

    def minus(self, that: Vector2D) -> Vector2D:
        return self.plus(that.scale(-1))

    def plus(self, that: Vector2D) -> Vector2D:
        return Vector2D(self.x + that.x, self.y + that.y)
