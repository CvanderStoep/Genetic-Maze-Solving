"""Provides a small Tkinter form for entering simulation settings such as maze size, population size, move count, and number of simulations. It launches the run and then displays the plot."""
import tkinter as tk
from tkinter import messagebox

try:
    from .simulation import run_simulation
except ImportError:  # pragma: no cover - allows running this file directly
    from simulation import run_simulation

FIELDS = [
    ("Maze size", "50"),
    ("Number of individuals", "128"),
    ("Number of moves", "100"),
    ("Number of simulations", "100"),
]


def main() -> None:
    root = tk.Tk()
    root.title("Input")
    entries = []
    for row, (label, default) in enumerate(FIELDS):
        tk.Label(root, text=label).grid(row=row, column=0, sticky="w", padx=8, pady=4)
        entry = tk.Entry(root)
        entry.insert(0, default)
        entry.grid(row=row, column=1, padx=8, pady=4)
        entries.append(entry)

    def on_run() -> None:
        try:
            values = [int(e.get()) for e in entries]
        except ValueError:
            messagebox.showerror("Invalid input", "All fields must be whole numbers.")
            return
        root.destroy()
        # matplotlib and tkinter must share the main thread, so run after closing the form.
        run_simulation(*values)
        import matplotlib.pyplot as plt
        plt.show()

    tk.Button(root, text="Run", command=on_run).grid(row=len(FIELDS), column=0, columnspan=2, pady=8)
    root.mainloop()


if __name__ == "__main__":
    main()
