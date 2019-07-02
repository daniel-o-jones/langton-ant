"""
Langton's Ant

s4536536
Daniel Jones
"""

import numpy as np

class LangtonAnt:
    '''
    Object for computing Langton's ant game
    '''
    def __init__(self, N=100, states = 2, rules = [1,-1]):
        self.grid = np.zeros((N,N), np.uint)
        self.direction = 0 #0 north, 1 east, 2 south, 3 west
        self.antLocation = (int(N/2), int(N/2))
        self.states = states
        self.rules = rules

    def getStates(self):
        return self.grid

    def step(self):
        antX = self.antLocation[0]
        antY = self.antLocation[1]
        antCurrent = self.grid[antX, antY]
        self.direction = (self.direction + self.rules[antCurrent]) % 4
        self.grid[antX, antY] = (self.grid[antX, antY] + 1) % self.states
        if (self.direction == 0):
            self.antLocation = (antX, antY + 1)
        elif (self.direction == 1):
            self.antLocation = (antX + 1, antY)
        elif (self.direction == 2):
            self.antLocation = (antX, antY - 1)
        else:
            self.antLocation = (antX-1, antY)

ant_states = 3
    
ant = LangtonAnt(N = 100, states = ant_states, rules=[1,-1,1])
cells = ant.getStates()

ant.step()
for i in range(1000):
    ant.step()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

fig = plt.figure()

plt.gray()

cmap = colors.ListedColormap(['red', 'blue', 'green', 'yellow', 'purple','orange'])

img = plt.imshow(cells,cmap = cmap, animated=True,vmin=0,vmax=ant_states)

def animate(i):

    global ant

    ant.step()
    cellsUpdated = ant.getStates()
    
    img.set_array(cellsUpdated)
    return img,

interval = 1 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=100, interval=interval, blit=True)

plt.show()

