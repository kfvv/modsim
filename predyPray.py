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
    def __init__(self, pos):
        self.pos = pos
        self.health = 100


class Prey(Animal):
    color = PREY


class Predator(Animal):
    color = PREDATOR


class Cell(object):
    color = EMPTY


def plot(grid, preys, predators):
    grid[:, :] = EMPTY

    for prey in preys:
        grid[prey.pos] = PREY

    for predator in predators:
        grid[predator.pos] = PREDATOR


def random_walk_animal(animal):
    move = random.randint(0, 3)
    x, y = animal.pos

    if move == 0:
        x, y = (x, y - 1)
    elif move == 1:
        x, y = (x - 1, y)
    elif move == 2:
        x, y = (x, y + 1)
    elif move == 3:
        x, y = (x + 1, y)

    animal.pos = x, y


if __name__ == '__main__':
    # Make the simulation deterministic
    random.seed(42)

    N = 24
    T = 10

    prey_count = 10
    predator_count = 3

    grid = np.zeros((N, N))

    # Select the cells where preys or predators are stored initially
    cells = random.sample([(i, j) for i in range(N) for j in range(N)],
                          prey_count + predator_count)

    preys = map(Prey, cells[:prey_count])
    predators = map(Predator, cells[prey_count:])

    # Start the model evaluation
    for t in range(T):
        plot(grid, preys, predators)
        plt.imshow(grid, interpolation='nearest', cmap=cmap, norm=norm)
        plt.pause(0.1)

        # Update the predator-prey model
        random_walk_animal(preys[0])
