"""Represents one candidate solution in the genetic algorithm. It tracks the individual’s start position, target, current end position, movement path, and fitness score, and includes mutation and crossover behavior."""

from __future__ import annotations

import random

from .genetic_code import GeneticCode
from .maze import Maze
from .move import Move
from .vector2d import Vector2D

MUTATION_PERCENTAGE = 5


class Individual:
    def __init__(self, maze_size: int) -> None:
        self.start_location = Vector2D(1, 1)
        self.target_location = Vector2D(maze_size - 1, maze_size - 1)
        self.genetic_code = GeneticCode()
        self.end_location = self.start_location
        self.trajectory_of_positions: list[Vector2D] = []
        self.maze_size = maze_size

    def fitness(self) -> float:
        return self.end_location.distance_to(self.target_location)

    def update_position(self, mz: Maze) -> None:
        self.end_location = self.start_location
        self.trajectory_of_positions.clear()
        self.trajectory_of_positions.append(self.start_location)
        for mv in self.genetic_code.moves:
            old_end_location = self.end_location
            self.end_location = self.end_location.plus(mv.direction)

            x_end = int(self.end_location.x)
            y_end = int(self.end_location.y)

            if not mz.is_open(x_end, y_end):
                self.end_location = old_end_location
            self.trajectory_of_positions.append(self.end_location)

    def random_mutation(self) -> None:
        mutated = GeneticCode()
        for mv in self.genetic_code.moves:
            if random.randrange(100) < MUTATION_PERCENTAGE:
                mutated.moves.append(Move.get_random_move())
            else:
                mutated.moves.append(mv)
        self.genetic_code = mutated

    def cross_over(self, individual2: Individual, cross_over_point: int) -> list[Individual]:
        child1 = Individual(self.maze_size)
        child2 = Individual(self.maze_size)
        for index, move1 in enumerate(self.genetic_code.moves):
            move2 = individual2.genetic_code.moves[index]
            if index < cross_over_point:
                child1.genetic_code.moves.append(move1)
                child2.genetic_code.moves.append(move2)
            else:
                child2.genetic_code.moves.append(move1)
                child1.genetic_code.moves.append(move2)
        # As in the Java original only child1 is mutated.
        child1.random_mutation()
        return [child1, child2]


def main() -> None:
    new_i = Individual(3)
    ngc = GeneticCode()
    mz = Maze(3, 3)
    ngc.moves.extend([Move.RIGHT, Move.UP, Move.UP, Move.UP, Move.UP])
    new_i.genetic_code = ngc
    new_i.update_position(mz)

    print(new_i.start_location)
    print(ngc.moves)
    print(new_i.end_location)
    print(new_i.fitness())
    new_i.random_mutation()
    print(new_i.genetic_code.moves)
    print(len(ngc.moves))


if __name__ == "__main__":
    main()
