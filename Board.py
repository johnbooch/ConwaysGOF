import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

from Exceptions import GOFException
import Patterns
import time


class Board(object):
    
    BOARD_PADDING = 10
    
    def __init__(self, update, world="random"):
        self.update = update
        self.world = world
        self.genWorld = getattr(self, 'gen' + world.title() + "World")
        
        self.fig = None
        self.X = None
        self.frame = 0

    def genRandomWorld(self, opts):
        self.X = np.random.randint(2, size=(opts.rows, opts.cols))
        return self.X
    
    def genEmptyWorld(self, opts):
        self.X = np.random.randint(1, size=(opts.rows, opts.cols))
        return self.X

    def genPatternWorld(self, opts):
        self.genEmptyWorld(opts)
        pattern = getattr(Patterns, opts.pattern.upper())
        self.blit(pattern, opts)
        return self.X

    def genRleWorld(self, opts):
        with open(opts.rle) as rle:
            pattern = Patterns.RLEPattern(rle)
            opts.rows, opts.cols = [dim + Board.BOARD_PADDING for dim in pattern.getSize()]
            opts.xy = [Board.BOARD_PADDING/2,Board.BOARD_PADDING/2]
            self.genEmptyWorld(opts)
            self.blit(pattern, opts)
            return self.X

    def blit(self, sprite, opts):
        (r,c) = sprite.getSize()
        (x, y) = opts.xy

        if (x, r, x+r) >= (opts.rows, opts.rows, opts.rows) or (y, c, y+c) >= (opts.cols, opts.cols, opts.cols):
            raise GOFException("Selected pattern is too large for world size or selected position is clipping pattern")
        
        self.X[x:x+r, y:y+c] = sprite.getPattern()

    def startAnimation(self, opts):

        self.fig = plt.figure("Conway's Game of Life")

        def init():
            if self.genWorld is None:
                raise GOFException("Generation function not initialzed")
            self.img = plt.imshow(self.genWorld(opts), interpolation='none', cmap=getattr(plt.cm, opts.cmap), vmax=1, vmin=0)
            self.img.set_data(self.X)
            return (self.img, )

        def animate(framedata):
            if self.update is None:
                raise GOFException("Update function not initialized")
            self.img.set_data(self.X)
            self.X = self.update(self.X)
            self.frame += 1
            return (self.img, )

        self.animation  = animation.FuncAnimation(self.fig,
                                  animate, init_func=init,
                                  interval=opts.framedelay)
        
        plt.show()