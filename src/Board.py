import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import patches

from Exceptions import GOFException
from Stopwatch import Stopwatch
import Patterns

class Board(object):
    
    BOARD_PADDING = 10
    FRAME_TITLE = "World: {world} Size: {size} Algorithm: {alg} Frame: {frame}"
    BOARD_TITLE = "Conway's Game of Life"
    TIME_FORMAT_HEADER = "{:20} {:20} {:20} {:20} {:20}\n".format('Time', 'Word Type', 'Percent Alive', 'World Size', 'Algorithm')
    TIME_FORMAT = "{time:<20} {world:<20} {alive:<20} {size:<20} {alg:<20}\n"
    TIME_FILE_REL_PATH = "time/time.txt"
    def __init__(self, update, world="random"):
        self.update = update
        self.world = world
        self.genWorld = getattr(self, 'gen' + world.title() + "World")
        
        self.fig = None
        self.X = None
        self.frame = 0
        self.timer = Stopwatch()

    def genRandomWorld(self, opts):
        self.X = np.random.choice([0,1] , size=(opts.rows, opts.cols), p=[1-(opts.percentage/100.0), opts.percentage/100.0])
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

        self.fig = plt.figure(Board.BOARD_TITLE)
        self.ax = self.fig.add_subplot(111)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.cmap = getattr(plt.cm, opts.cmap)


        def init():
            if self.genWorld is None:
                raise GOFException("Generation function not initialzed")
            self.img = plt.imshow(self.genWorld(opts), interpolation='none', cmap=self.cmap, vmax=1, vmin=0)
            self.img.set_data(self.X)
            legend_patches  = [patches.Patch(color=self.cmap(0), label='Dead'), patches.Patch(color=self.cmap(255), label='Alive')]
            self.fig.legend(handles=legend_patches)
            plt.title(Board.FRAME_TITLE.format(world=self.world.title(), size=np.prod(self.X.shape), alg=opts.algorithm.title(), frame=self.frame), fontsize=10)
            return (self.img, )

        def animate(framedata):
            if self.update is None:
                raise GOFException("Update function not initialized")
            
            with self.timer:
                self.X = self.update(self.X)
            if opts.time: 
                self.timer.genTimeFile((Board.TIME_FORMAT_HEADER, Board.TIME_FORMAT), Board.TIME_FILE_REL_PATH, time=self.timer.totalTime, world=self.world, alive=opts.percentage, size=np.prod(self.X.shape), alg=opts.algorithm)
            
            self.img.set_data(self.X)
            self.frame += 1
            plt.title(Board.FRAME_TITLE.format(world=self.world.title(), size=np.prod(self.X.shape), alg=opts.algorithm.title(), frame=self.frame), fontsize=10)
            return (self.img, )

        self.animation  = animation.FuncAnimation(self.fig,
                                animate, init_func=init,
                                interval=opts.framedelay)
        plt.show()