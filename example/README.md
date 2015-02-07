quantize examples
=================

## Stdin => Quantize => Midi message.

In a DAW set 'sync' to Midi Out on a desired port.

Now add an midi instrument to listen to Midi In on the same port.

Run `q -i` to see the listen of input ports.

Find the port you used above in your DAW and set it's name as and environment variable (`QUANTIZE_PORT`)

```
cat notes.txt | q -b 1/16 | python play.py
```
Try changing the bpm of your DAW and hear the difference!