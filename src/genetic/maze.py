"""Implements the maze grid, including open/blocked cells and plotting support for visualizing individuals, obstacles, and trajectories with matplotlib."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .individual import Individual


class Maze:
    def __init__(self, n_x: int, n_y: int) -> None:
        self.size_x = n_x
        self.size_y = n_y
        self._field = [[True] * n_y for _ in range(n_x)]

    def is_open(self, i: int, j: int) -> bool:
        if i < 0 or j < 0:
            return True
        if i >= self.size_x or j >= self.size_y:
            return False
        return self._field[i][j]

    def set_open(self, i: int, j: int, is_open: bool) -> None:
        if 0 <= i < self.size_x and 0 <= j < self.size_y:
            self._field[i][j] = is_open
        else:
            raise ValueError(f"The indices given ({i},{j}) were out of bounds.")

    def plot(self, individuals: list[Individual], generation: int, pause: float = 0.001) -> None:
        """Draw the population with matplotlib (replacement for StdDraw)."""
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle

        print("plotting...")

        fig = plt.figure("Genetic swarm")
        fig.clf()
        ax = fig.add_subplot(111)
        ax.set_xlim(0, self.size_x + 5)
        ax.set_ylim(0, self.size_y + 5)
        ax.set_aspect("equal")

        for ind in individuals:
            x_start = int(ind.start_location.x)
            y_start = int(ind.start_location.y)
            ax.add_patch(Circle((x_start, y_start), 0.2, color="blue"))

            # end location
            ax.add_patch(Circle((int(ind.end_location.x), int(ind.end_location.y)), 0.2, color="black"))

            # target location
            ax.add_patch(Circle((int(ind.target_location.x), int(ind.target_location.y)), 0.2, color="green"))

            # trajectory
            for cp in ind.trajectory_of_positions:
                xcp, ycp = int(cp.x), int(cp.y)
                ax.plot([x_start, xcp], [y_start, ycp], color="blue", linewidth=0.5)
                x_start, y_start = xcp, ycp

        ax.text(self.size_x // 2, self.size_y, f"fitness: {individuals[0].fitness():.2f}", ha="center")
        ax.text(self.size_x // 2, self.size_y + 1, f"generation: {generation}", ha="center")

        # blocked cells
        for i in range(self.size_x):
            for j in range(self.size_y):
                if not self.is_open(i, j):
                    ax.add_patch(Circle((i, j), 0.2, color="red"))

        fig.canvas.draw_idle()
        plt.pause(pause)
