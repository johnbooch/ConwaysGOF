import errno
import os
import time
import sys

class Stopwatch(object):

    STOPPED_ASSERTION = "Can not measure elapsed time on stopped Stopwatch instance"

    def __init__(self):
        self.startTime = None
        self.stopTime = None

    def start(self):
        self.startTime = time.time()

    def stop(self):
        self.stopTime = time.time()

    def reset(self):
        self.startTime = None
        self.stopTime = None

    @property
    def timeElapsed(self):
        assert not self.stopTime, Stopwatch.STOPPED_ASSERTION
        return time.time() - self.startTime

    @property
    def totalTime(self):
        return self.stopTime - self.startTime

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()
        if type:
            raise type, value, traceback

    def genTimeFile(self, (header, msg), filename, **kwargs):
        path = os.path.join(os.path.sep, os.getcwd(), filename)
        if not os.path.exists(os.path.dirname(path)): # Create directory for time file if it does not exists
            try:
                os.makedirs(os.path.dirname(path))
                with open(path, 'a+') as f:
                    f.write(header)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise  
        with open(path, 'a+') as f:
            f.write(msg.format(**kwargs))