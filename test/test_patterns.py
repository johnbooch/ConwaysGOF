import subprocess
import os
import time

def test(cmds, exec_time):
    for cmd in cmds:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(exec_time) # Allow simulation to run for 10 seconds
        p.terminate()


COMMANDS = [
    ["python src/gof.py --world rle --rle RLE/p-45-engine.rle --alg conv --cmap copper"],
    ["python src/gof.py --world rle --rle RLE/p65-glider-loop.rle--alg conv --cmap rainbow --framedelay 1"],
    ["python src/gof.py --rows 500 cols 500 --world random --perc 80 --alg roll --cmap copper --framedelay 1"],
    ["python src/gof.py --world rle --rle RLE/low-period.rle --alg conv --cmap rainbow --framedelay 1"],
    ["python src/gof.py --world rle --rle RLE/112P52.rle --alg conv --cmap winter --framedelay 1"],
    ["python src/gof.py --rows 100 --cols 50 --world pattern --pattern gosper_gun --cmap magma --framedelay 1"]
]

def main(): 
    test(COMMANDS, 10)

if __name__ == '__main__':
    main()