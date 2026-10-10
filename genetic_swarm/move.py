"""Defines the possible movement directions for an individual: left, right, up, down, and none. It uses an Enum and includes a random move generator."""

from __future__ import annotations

import random
from enum import Enum

from .vector2d import Vector2D


class Move(Enum):
    NONE = Vector2D(0, 0)
    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    UP = Vector2D(0, 1)
    DOWN = Vector2D(0, -1)

    @property
    def direction(self) -> Vector2D:
        return self.value

    @staticmethod
    def get_random_move() -> Move:
        return random.choice(list(Move))
