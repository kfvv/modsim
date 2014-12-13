import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import animation
import numpy as np
import random

EMPTY = 0
PREDATOR = 1
PREY = 2

# Make a colormap of fixed colors using:
# http://stackoverflow.com/questions/9707676/defining-a-discrete-colormap-for-imshow-in-matplotlib
cmap = colors.ListedColormap(['white', 'red', 'blue'])
bounds = [EMPTY, PREDATOR, PREY, 3]
norm = colors.BoundaryNorm(bounds, cmap.N)


class Animal:
    def __init__(self, health):
        self.health = health


class Prey(Animal):
    color = PREY


class Predator(Animal):
    color = PREDATOR


class Cell(object):
    color = EMPTY


def plot(grid):
    plt.imshow(grid, interpolation='nearest', cmap=cmap, norm=norm)
    plt.show()


if __name__ == '__main__':
    # Make the simulation deterministic
    random.seed(42)

    N = 24

    prey_count = 10
    predator_count = 3

    grid = np.zeros((N, N))

    # Select the cells where preys or predators are stored initially
    amount = prey_count + predator_count
    cells = random.sample([(i, j) for i in range(N) for j in range(N)], amount)

    print('prey:', cells[:prey_count])
    print('predator:', cells[prey_count:])

    for x, y in cells[:prey_count]:
        grid[x, y] = PREY

    for x, y in cells[prey_count:]:
        grid[x, y] = PREDATOR

    plot(grid)
