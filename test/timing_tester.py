import subprocess
import os
import time

def test(cmds, exec_time):
    for cmd in cmds:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(exec_time) # Allow simulation to run for 10 seconds
        p.terminate()

COMMANDS_50x50 = [
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 25 --alg linear --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 25 --alg roll --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 25 --alg conv --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 25  --alg set --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 50 --alg linear --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 50 --alg roll --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 50 --alg conv --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 50 --alg set --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 75 --alg linear --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 75 --alg roll --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 75 --alg conv --time"],
    ["python src/gof.py --rows 50 --cols 50 --world random --perc 75 --alg set --time"],
]

COMMANDS_100x100 = [
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 25 --alg linear --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 25 --alg roll --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 25 --alg conv --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 25  --alg set --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 50 --alg linear --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 50 --alg roll --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 50 --alg conv --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 50 --alg set --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 75 --alg linear --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 75 --alg roll --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 75 --alg conv --time"],
    ["python src/gof.py --rows 100 --cols 100 --world random --perc 75 --alg set --time"],
]

COMMANDS_500x500 = [
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 25 --alg linear --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 25 --alg roll --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 25 --alg conv --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 25  --alg set --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 50 --alg linear --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 50 --alg roll --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 50 --alg conv --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 50 --alg set --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 75 --alg linear --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 75 --alg roll --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 75 --alg conv --time"],
    ["python src/gof.py --rows 500 --cols 500 --world random --perc 75 --alg set v"],
]

COMMANDS_1000x1000 = [
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 25 --alg linear --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 25 --alg roll --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 25 --alg conv --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 25  --alg set --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 50 --alg linear --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 50 --alg roll --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 50 --alg conv --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 50 --alg set --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 75 --alg linear --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 75 --alg roll --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 75 --alg conv --time"],
    ["python src/gof.py --rows 1000 --cols 1000 --world random --perc 75 --alg set --time"],
]

def main():
    test(COMMANDS_50x50, 5)
    test(COMMANDS_100x100, 10)
    test(COMMANDS_500x500, 20)
    test(COMMANDS_1000x1000, 25)


if __name__ == "__main__":
    main()