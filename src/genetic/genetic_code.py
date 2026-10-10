"""Defines a genetic code as a list of movement commands. It creates random codes for individuals and stores the sequence of moves that an agent will follow."""

from __future__ import annotations

from .move import Move


class GeneticCode:
    def __init__(self) -> None:
        self.moves: list[Move] = []

    @staticmethod
    def generate_random_code(number_of_moves: int) -> GeneticCode:
        code = GeneticCode()
        for _ in range(number_of_moves):
            code.moves.append(Move.get_random_move())
        return code
