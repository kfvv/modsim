import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import animation
import random


# Make a colormap of fixed colors using http://stackoverflow.com/questions/
# 9707676/defining-a-discrete-colormap-for-imshow-in-matplotlib
cmap = colors.ListedColorMap(['white', 'red', 'green'])
bounds = [EMPTY, PREDATOR, PRAY, 3]
norm = colors.BoundaryNorm(bounds, cmap.N)

class predPray:
    specie = 2
    PREY, PREDATOR = range(specie)

    def health(self, energy):
        self.health = health;


    def healthDecr(self, val):
        self.health -= val;

    def healthIncr(self, val):
        self.health += val;

    def getHealth(self):
        return self.energy

    def getChar(self):
        return self.char

class prey(object):
    def health(self):


class predator(object):

    def health(self):

class cell(object):
    def __init__(self):
        self.content = None

    def place(self, animal):
        self.content = animal
        animal.cell = self

class grid(object):
    def __init_(self, X, N_prey, N_predator):
        self.cells = [[cell() for j in range(X)] for i in range(X)]


    for i in range(X):
        for j in range(X):
            self.cells[i][j].neighbours = (self.cells[i](j + 1) % X],
                                            (self.cells[i](j - 1) % X],
                                             (self.cells[i](j + 1) % X],
                                            (self.cells[(i - 1) % X][j]

    self.allpray = [prey() for i in range(N_prey)]
    self.allpredator = [predator() for i in range(N_predator)]


    empty = [gridcell for row in self.cells for gridcell in row]

    for animal in self.allprey + self.allpredator:
        randomcell = empty.pop(random.randrange(len(empty)))

        randomcell.place(animal)

if __name__ = '__main__':
