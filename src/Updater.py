import numpy as np
import time

class Updater(object): 

    def __init__ (self, algorithm='linear'):
        self.alg = algorithm
        self.update = getattr(self, algorithm + 'Update')

    def linearUpdate(self, X):
        state = sum(np.roll(np.roll(X, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
        return (state == 3) | (X & (state == 2))

    def convUpdate(self, X):
        from scipy.signal import convolve2d
        state = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
        return (state == 3) | (X & (state == 2))
    
    def mpiUpdate(self, X):
        pass