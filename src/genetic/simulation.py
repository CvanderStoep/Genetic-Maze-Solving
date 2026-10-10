"""Runs the evolutionary simulation loop. It creates the population, adds obstacles, keeps the strongest individuals, performs crossover, and repeats generations while optionally plotting progress."""

from __future__ import annotations

import argparse
import random
import time

from .genetic_code import GeneticCode
from .individual import Individual
from .maze import Maze


class Simulation:
    def __init__(self, maze_size: int, number_of_individuals: int, number_of_moves: int) -> None:
        self.maze_size = maze_size
        self.mz = Maze(maze_size, maze_size)
        self.number_of_individuals = number_of_individuals
        self.number_of_moves = number_of_moves
        self.individuals: list[Individual] = []

        for _ in range(number_of_individuals):
            individual = Individual(maze_size)
            individual.genetic_code = GeneticCode.generate_random_code(number_of_moves)
            individual.update_position(self.mz)
            self.individuals.append(individual)

    def add_obstacles(self) -> None:
        for i in range(5, 10):
            for j in range(5, 10):
                self.mz.set_open(i, j, False)
        for i in range(15, 20):
            for j in range(5, 20):
                self.mz.set_open(i, j, False)

    def cross_over(self) -> None:
        next_individual = 0
        while next_individual < self.number_of_individuals // 2:
            cross_over_point = random.randrange(self.number_of_moves) + 1
            in1 = self.individuals[next_individual]
            in2 = self.individuals[next_individual + 1]
            self.individuals.extend(in1.cross_over(in2, cross_over_point))
            next_individual += 2
        for individual in self.individuals:
            individual.update_position(self.mz)

    def run(self, number_of_simulations: int, plot: bool = True, delay: float = 0.2) -> None:
        self.individuals.sort(key=Individual.fitness)
        print("sorted: ")
        self.add_obstacles()

        for i in range(number_of_simulations):
            # kill the weaker half
            del self.individuals[len(self.individuals) // 2:]
            print(f"generation: {i}")
            print("killed 1/2: ")
            self.cross_over()
            self.individuals.sort(key=Individual.fitness)
            print("crossover: ")
            print(f"best fitness: {self.individuals[0].fitness():.2f}")
            if plot:
                self.mz.plot(self.individuals, i)
            time.sleep(delay)


def run_simulation(maze_size: int, number_of_individuals: int, number_of_moves: int,
                   number_of_simulations: int, plot: bool = True, delay: float = 0.2) -> Simulation:
    print("started: ")
    sim = Simulation(maze_size, number_of_individuals, number_of_moves)
    sim.run(number_of_simulations, plot=plot, delay=delay)
    return sim


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Genetic swarm simulation")
    parser.add_argument("maze_size", type=int)
    parser.add_argument("number_of_individuals", type=int)
    parser.add_argument("number_of_moves", type=int)
    parser.add_argument("number_of_simulations", type=int)
    parser.add_argument("--no-plot", action="store_true", help="run without the matplotlib window")
    args = parser.parse_args(argv)
    run_simulation(args.maze_size, args.number_of_individuals, args.number_of_moves,
                   args.number_of_simulations, plot=not args.no_plot,
                   delay=0.0 if args.no_plot else 0.2)
    if not args.no_plot:
        import matplotlib.pyplot as plt
        plt.show()


if __name__ == "__main__":
    main()
