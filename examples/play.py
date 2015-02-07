import subprocess
import sys
import os
import mido
import time

import msg

# unbuffered readers
sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 1)

def main():
    try:
        while True:
            msg = sys.stdin.readline()
            note, velocity, duration = msg.split(' ')
            subprocess.Popen(['python', 'msg.py', note, velocity, duration])
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
