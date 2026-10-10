# Genetic_Swarm (Python port)

Python port of the Java project [CvanderStoep/Genetic_Swarm](https://github.com/CvanderStoep/genetic_swarm).

A population of individuals tries to reach a target position in a 2D maze. Each individual has a genetic code (a sequence of moves). After each generation the fitter half survives, offspring are created by crossover, and 5% of the moves of one child are mutated.

## Setup

    pip install -r requirements.txt

## Run

    # GUI input form (tkinter) followed by a live matplotlib plot
    PYTHONPATH=src .venv/bin/python -m genetic.input_gui

    # command line: maze_size individuals moves generations
PYTHONPATH=src .venv/bin/python -m genetic.simulation 50 128 100 100
PYTHONPATH=src .venv/bin/python -m genetic.simulation 50 128 100 100 --no-plot # headless


    # plot the USA outline data
PYTHONPATH=src .venv/bin/python -m genetic.plot_filter inp/USA.txt

    # tests
    pytest

## Mapping from Java

| Java | Python |
|------|--------|
| Vector2D, Move, GeneticCode, Maze, Individual, Simulation | `genetic_swarm/*.py` (snake_case) |
| Input (Swing form) | `input_gui.py` (tkinter) |
| StdDraw / PlotFilter | matplotlib |
| MazeTest (JUnit) | `tests/test_maze.py` (pytest) |

Behaviour is kept as in the original, including: fitness is the *squared* distance (`Vector2D.magnitude` never takes a square root), only one of the two children is mutated, and negative coordinates count as open.
