import numpy as np
from scipy.signal import convolve2d

class Updater(object): 

    def __init__ (self, algorithm='linear'):
        self.alg = algorithm
        self.update = getattr(self, algorithm + 'Update')

    def linearUpdate(self, X):
        width, height = X.shape
        Y = np.copy(X) # Gets rid of (neighbors == 2 and already alive state)
        for y in range(height):
            for x in range(width):
                neighbors = sum([X[(x_coord) % (width)][(y_coord) % (height)] for x_coord, y_coord in self.neighbors((x,y))])
                if (neighbors < 2):
                    Y[x][y] = 0
                if (neighbors > 3):
                    Y[x][y] = 0
                if (neighbors == 3):
                    Y[x][y] = 1
        return Y

    def rollUpdate(self, X):
        neighbors = sum(np.roll(np.roll(X, i, 0), j, 1)
                     for i in [-1, 0, 1] for j in [-1, 0, 1] if (i != 0 or j != 0))
        return (neighbors == 3) | (X & (neighbors == 2))

    def convUpdate(self, X):
        neighbors = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
        return (neighbors == 3) | (X & (neighbors == 2))
    
    def setUpdate(self, X):
        width, height = X.shape
        X_set = self.boardToSet(X)
        Y_set = set([])
        cells = X_set.union(set(((x % (width), y % (height)) for cell in X_set for x,y in self.neighbors(cell))))
        for cell in cells:
            neighbors = sum(((x % (width), y % (height)) in X_set ) for x,y in self.neighbors(cell))
            if (neighbors == 3 or (neighbors == 2 and cell in X_set)):
                Y_set.add((cell[0], cell[1]))
        return self.setToBoard(Y_set, X.shape)

    def boardToSet(self, X):
        return set(zip(*np.where(X==1)))

    def setToBoard(self, X_set, size):
        X = np.zeros(size)
        X[zip(*list(X_set))] = 1
        return X

    def neighbors(self, xy):
        x, y = xy
        yield x - 1, y - 1
        yield x    , y - 1
        yield x + 1, y - 1
        yield x - 1, y
        yield x + 1, y
        yield x - 1, y + 1
        yield x    , y + 1
        yield x + 1, y + 1

