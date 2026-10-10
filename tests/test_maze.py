"""Contains tests for maze behavior, including checking whether cells are open or blocked and ensuring out-of-bounds writes raise an error."""

import pytest

from genetic_swarm.maze import Maze


def test_is_open():
    a_maze = Maze(10, 10)
    assert a_maze.is_open(0, 0)
    assert a_maze.is_open(1, 1)
    assert a_maze.is_open(9, 9)
    assert not a_maze.is_open(10, 10)
    assert a_maze.is_open(-1, 0)


def test_set_open():
    a_maze = Maze(10, 10)

    a_maze.set_open(0, 0, False)
    assert not a_maze.is_open(0, 0)
    a_maze.set_open(0, 0, True)
    assert a_maze.is_open(0, 0)

    a_maze.set_open(9, 9, False)
    assert not a_maze.is_open(9, 9)
    a_maze.set_open(9, 9, True)
    assert a_maze.is_open(9, 9)


def test_set_open_out_of_bounds():
    with pytest.raises(ValueError):
        Maze(10, 10).set_open(10, 0, False)
