from __future__ import print_function
"""
 Author: John Buccieri
"""
import numpy as np
import re

class Pattern(object):
        def __init__(self, X):
                self.X = np.asarray(X)
                
        def getSize(self):
                return np.shape(self.X)

        def getPattern(self):
                return np.asarray(self.X)
        
        def __str__(self):
                return str(self.X)
        
class Still(Pattern):
        def __init__(self, X):
                super(Still, self).__init__(X)

class Oscillator(Pattern):
        def __init(self, X):
                super(Oscillator, self).__init__(X)

class Glider(Pattern):
        def __init(self, X):
                super(Glider, self).__init__(X)

class Generator(Pattern):
        def __init(self, X):
                super(Generator, self).__init__(X)

class RLEPattern(Pattern):

        def __init__(self, file):
                self.comments = []
                self.dims = []
                super(RLEPattern, self).__init__(self.decode(file.read()))
        
        def decode(self, data):
                self.comments  = re.findall(r'^[#;].*', data); data = re.sub(r'^[#;].*', '', data)
                self.dims =  [int(el[:-1]) for el in re.findall(r'(\d+,)', data)]; data= re.sub(r'x.*=.*', '', data) #TODO Fix this regex, it is sloppy
                return [self.decompress(line) for line in re.findall(r'.*?[?=$]', data.replace('\n', '').replace('!', '$'))]
        
        def decompress(self, data):
                decompressed = [0] * self.dims[0]
                index = 0
                for code in re.findall(r'.*?[?=b|o|$]', data):
                        if code is '$': continue
                        num, state = RLEPattern.RLETagConv(re.split(r'(b|o|\$)', code))
                        decompressed[index: index+num] = [state]*num
                        index += num
                return decompressed
        
        @staticmethod
        def RLETagConv(tag):
                num, state, _ = tag
                num = 1 if num == '' else int(num)
                state = 1 if state == 'o' else 0 if state == 'b' else '$'
                return (num, state)


''' Stills'''
BLOCK = Still([[1, 1],
               [1, 1]])

LOAF = Still([[0, 1, 1, 0],
              [1, 0, 0, 1],
              [0, 1, 1, 0]])

BEEHIVE = Still([[0, 1, 1, 0],
                 [1, 0, 0, 1],
                 [1, 0, 1, 0],
                 [0, 1, 0, 0]])

BOAT = Still([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])


'''Oscillators'''
BLINKER = Oscillator([[0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0]])
        
TOAD =  Oscillator([[1, 1, 1, 0],
                    [0, 1, 1, 1]])


'''Gliders'''
GLIDER = Glider([[0, 0, 1],
          [1, 0, 1],
          [0, 1, 1]])

'''Generators'''
GOSPER_GUN = Generator([
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
