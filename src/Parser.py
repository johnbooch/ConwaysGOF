from argparse import ArgumentParser
def createDefaultParser():
    """
    Accepts: (Nothing)

    Returns: parser -- default GOF argument parser
    """
    parser = ArgumentParser()

    parser.add_argument('-r', '--rows',
                        help='set number of rows in the world',
                        action='store',
                        type=int,
                        dest='rows',
                        default=50)

    parser.add_argument('-c', '--cols',
                        help='set number of columns in the world',
                        action='store',
                        type=int,
                        dest='cols',
                        default=50)

    parser.add_argument('-w', '--world',
                        help='type of world to generate. Options are random, empty, pattern, RLE',
                        action='store',
                        type=str,
                        dest='world',
                        default='random')

    parser.add_argument('-p', '--pattern',
                        help='pattern to be used in pattern world generation. See patterns file',
                        action='store',
                        type=str,
                        dest='pattern',
                        default='glider')

    parser.add_argument('-perc', '--percentage',
                    help='percentage of world to be populated on random world generation',
                    action='store',
                    type=float,
                    dest='percentage',
                    default=10.0)
    
    parser.add_argument('-xy', '--xy',
                        help='(X,Y) coords where pattern will be inserted',
                        action='store',
                        type=int,
                        nargs=2,
                        dest='xy',
                        default=[0,0])
    
    parser.add_argument('-rle','--rle',
                        help='path of RLE file to be loaded',
                        action='store',
                        type=str,
                        dest='rle')

    parser.add_argument('-a', '--algorithm',
                        help='update algorithm to be used. Options are: linear, set, roll, conv',
                        action='store',
                        type=str,
                        default="linear",
                        dest='algorithm')

    parser.add_argument('-d', '--framedelay',
                        help='time (in milliseconds) between frames',
                        action='store',
                        type=int,
                        dest='framedelay',
                        default=100)
                        
    parser.add_argument('-cmap', '--cmap',
                        help='color map of grid. See matplotlib for options',
                        action='store',
                        type=str,
                        dest='cmap',
                        default='binary')
    
    parser.add_argument('-t', '--time',
                    help='generates output file for timing of selected update algorithm',
                    action='store_true',
                dest='time')
    return parser