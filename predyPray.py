import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random

EMPTY = 0
PREDATOR = 1
PREY = 2

# Species procreate when their energy exceeds this threshold
HEALTH_SPLIT_THRESHOLD = 60

# Make a colormap of fixed colors using:
# http://stackoverflow.com/questions/9707676/defining-a-discrete-colormap-for-imshow-in-matplotlib
cmap = colors.ListedColormap(['white', 'red', 'blue'])
bounds = [EMPTY, PREDATOR, PREY, 3]
norm = colors.BoundaryNorm(bounds, cmap.N)


class Animal:
    def __init__(self):
        self.health = 10


class Prey(Animal):
    grid_code = PREY

    def __repr__(self):
        return 'Prey'


class Predator(Animal):
    grid_code = PREDATOR

    def __repr__(self):
        return 'Predator'

    def eat(self, prey):
        self.health += prey.health


def plot(grid, pos):
    grid[:, :] = EMPTY

    for (x, y), animal in pos.iteritems():
        grid[x, y] = animal.grid_code


def random_walk_animal(grid, cur_x, cur_y, animal, pos):
    height, width = grid.shape

    while True:
        move = random.randint(0, 3)

        x = cur_x
        y = cur_y

        if move == 0:
            x, y = (x, y + 1)
        elif move == 1:
            x, y = (x + 1, y)
        elif move == 2:
            x, y = (x, y - 1)
        elif move == 3:
            x, y = (x - 1, y)

        if 0 <= x < width and 0 <= y < height:
            break

    if isinstance(animal, Predator):
        # Decrease the health of a predator after each time step.
        animal.health -= 1

        if animal.health > HEALTH_SPLIT_THRESHOLD:
            # Find position for the new predator.
            for i, j in [(cur_x, cur_y + 1), (cur_x + 1, cur_y),
                         (cur_x, cur_y - 1), (cur_x - 1, cur_y)]:
                if 0 <= i < width and 0 <= j < height and (i, j) not in pos:
                    animal.health /= 2

                    new_animal = Predator()
                    new_animal.health = animal.health
                    pos[i, j] = new_animal

        # Predator dies if it has no energy left.
        if animal.health <= 0:
            del pos[cur_x, cur_y]
            return

        if (x, y) in pos:
            target = pos[(x, y)]

            # Do not allow a predator to move on top of another predator.
            # Make sure that there is no infinite loop when a predator is
            # surrounded by other predators. Therefore, we let the predator
            # stay at its position for this move.
            if isinstance(target, Predator):
                return

            # If the predator moves on top of a prey, eat the prey and take
            # it's energy.
            if isinstance(target, Prey):
                animal.eat(pos[(x, y)])
                del pos[(x, y)]
    else:
        # Increase the health of a prey after each time step.
        animal.health += 1

        if animal.health > HEALTH_SPLIT_THRESHOLD:
            # Find position for the new prey.
            for i, j in [(cur_x, cur_y + 1), (cur_x + 1, cur_y),
                         (cur_x, cur_y - 1), (cur_x - 1, cur_y)]:
                if 0 <= i < width and 0 <= j < height and (i, j) not in pos:
                    animal.health /= 2

                    new_animal = Prey()
                    new_animal.health = animal.health
                    pos[i, j] = new_animal

        if (x, y) in pos:
            target = pos[(x, y)]

            # Do not allow a prey to move on top of another prey.  Make
            # sure that there is no infinite loop when a prey is surrounded
            # by other preys. Therefore, we let the prey stay at its
            # position for this move.
            if isinstance(target, Prey):
                return

            # If the prey moves on top of a predator, the predator eats the
            # prey and takes it's energy. The prey is dead.
            if isinstance(target, Predator):
                pos[(x, y)].eat(animal)
                del pos[(cur_x, cur_y)]
                return

    # Move the animal to its new position
    del pos[cur_x, cur_y]
    pos[(x, y)] = animal


if __name__ == '__main__':
    # Make the simulation deterministic
    random.seed(42)

    N = 24
    T = 100

    prey_count = 80
    predator_count = 25

    grid = np.zeros((N, N), dtype=int)

    # Select the cells where preys or predators are stored initially
    cells = random.sample([(i, j) for i in range(N) for j in range(N)],
                          prey_count + predator_count)

    # Make lookup table for preys and predators
    pos = {}

    for x, y in cells[:prey_count]:
        pos[(x, y)] = Prey()

    for x, y in cells[prey_count:]:
        pos[(x, y)] = Predator()

    # Start the model evaluation
    for t in range(T):
        plot(grid, pos)
        plt.imshow(grid, interpolation='nearest', cmap=cmap, norm=norm)
        plt.pause(0.1)

        # Update the predator-prey model
        for x, y in [(i, j) for i in range(N) for j in range(N)]:
            if (x, y) not in pos:
                continue

            animal = pos[(x, y)]
            random_walk_animal(grid, x, y, animal, pos)
