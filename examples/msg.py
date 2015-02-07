import mido
import time
import sys
import os

output = mido.open_output(os.getenv('QUANTIZE_PORT'))

def play_message(note, velocity, duration):
    output.send(mido.Message('note_on', note=int(note), velocity=int(velocity)))
    time.sleep(float(duration))
    output.send(mido.Message('note_off', note=int(note)))

if __name__ == '__main__':
	play_message(*sys.argv[1:])