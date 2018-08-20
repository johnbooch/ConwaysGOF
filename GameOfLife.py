from argparse import ArgumentParser

from Board import Board
from Updater import Updater
from Parser import createDefaultParser
from Exceptions import GOFException

class GameOfLife(object):
    def __init__(self):
        self.parser = createDefaultParser()

        # Initialize empty parameters
        self.opts = None
        self.updater = None
        self.board = None

    def createUpdater(self):
        if self.opts == None:
            raise GOFException("Program options have not been initialized") 
        self.updater = Updater(algorithm=self.opts.algorithm)
    
    def createBoard(self):
        if self.opts == None:
            raise GOFException("Program options have not been initialized")
        if self.updater == None:
            raise GOFException("Updater not initialized")
        self.board = Board(self.updater.update, world=self.opts.world) 

    def addCommandLineOpts(self, parser):
        self.parser = ArgumentParser(parents=[self.parser, parser])
    
    def getCommandLineOpts(self):
        self.opts = self.parser.parse_args()
    
    def run(self):
        self.getCommandLineOpts()
        self.createUpdater()
        self.createBoard()
        self.board.startAnimation(self.opts)

