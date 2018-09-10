"""
 Author: John  Buccieri
   A simple implementation of Conway's Game of Life
"""
import sys
import traceback

from GameOfLife import GameOfLife

def main():
    gof = GameOfLife()
    try:
        gof.run()
    except Exception as e:
        traceback.print_exc(e)
        return -1

if __name__ == '__main__':
    sys.exit(main())