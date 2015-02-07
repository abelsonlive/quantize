quantize
========

`quantize` is simple command line utility for quantizing arbitrary messages sent via `stdin` to a midi clock.

For each line of `stdin` it blocks until a tick at a specified beat has been recieved from a midi clock, it then writes this message to `stdout`.

You can see a full example [here](example/).

**NOTE** this doesn't work great, theres some latency issues probably because I'm using `python` and not `C` :/

## Installation
_Tested only on Mac OSX_

If you have trouble installing `python-rtmidi`, see the docs for [`mido`](http://mido.readthedocs.org/en/latest/installing.html)
```
$ brew install portmidi
$ pip install quantize
```

## Usage

List available input midi ports:

```bash
$ q -l 
>>> Available input ports:
>>> 'IAC Driver Bus 1'
>>> 'IAC Driver IAC Bus 2'
``` 

Quantize input lines:
(You can optionally set `QUANTIZE_PORT` as an environment variable.)

```bash
$ echo "1\n2\n3\n4" | q --port 'IAC Driver Bus 1' --beat 1/4
```

Full usage:

```
optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  The midi port on which to listen for clock messages.
  -b BEAT, --beat BEAT  The beat count to sync stdin to, e.g. "1/8", "1/4",
                        "1", etc
  -l LATENCY, --latency LATENCY
                        Number of clock ticks to offset quantization by.
  -i, --list-inputs     List available input midi ports and exit.
```

## TODO 

- [ ] Figure out how to exit process on EOF.
- [ ]
