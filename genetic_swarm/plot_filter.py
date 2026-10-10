"""Reads coordinate data from a file or stdin and plots the points on a graph. It is a utility for visualizing datasets in the format expected by the project."""
import sys

import matplotlib.pyplot as plt


def main() -> None:
    text = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    numbers = [float(t) for t in text.split()]
    x0, y0, x1, y1 = numbers[:4]
    coords = numbers[4:]
    xs, ys = coords[0::2], coords[1::2]

    fig, ax = plt.subplots()
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.scatter(xs, ys, s=2, color="black")
    plt.show()


if __name__ == "__main__":
    main()
