# Micropython Controller for testing [Oldwyk](https://github.com/hni-sct/pulpino-sdk#oldwyk)

## Building the Toolchain
First download the submodules by typing
```
$ git submodule update --init --recursive
```
then build the [freedom-e-sdk](https://github.com/hni-sct/freedom-e-sdk) by
```
$ make tools
```
If you have the [freedom-e-sdk](https://github.com/hni-sct/freedom-e-sdk) already installed, you can skip the steps above, but you need to set the environment variable FREEDOM_E for all steps below.

## Building the Micropython Firmware
Simply type
```
$ make firmware
```
Before uploading the firmware check chapter 5 of the [Getting Started
Guide](https://sifive.cdn.prismic.io/sifive%2F9c57065b-6d28-465b-b67d-f416894123a9_hifive1-getting-started-v1.0.2.pdf)
and check whether you can connect to the Hifive1. If you verified that you can
upload programs, then you can simply type:
```
$ make upload
```

## Micropython console
You can connect to the micropython REPL using screen:
```
screen /dev/ttyUSB1 115200
```
You should see a message like:
```
core freq at 285523968 Hz
MicroPython v1.9.3-776-g5d35f272-dirty on 2019-12-10; Arty FPGA Dev Kit with E310
Type "help()" for more information.
>>>
```
If not, press the reset button on the board or type `make upload` again.
To interact with Oldwyk first import the `python board library` (pyb)  by
typing on the REPL:
```
>>> import pyb
```
then create an SPI interface using a CS pin 7 (if you selected another pin
during wiring, replace the 7 with that pin) and a maximum SPI frequency of
25 Mhz.
```
>>> spi = pyb.SPI(7, 2500000, 0, 0)
```
Now you can toggle the LED:
```
>>> spi.write_mem(0x1A101000, (1 << 10))
>>> spi.write_mem(0x1A101008, (1 << 10))
>>> spi.write_mem(0x1A101008, 0)
```

## Upload micropython scripts
If you don't want to type all commands repeatedly on the REPL you can upload
them using the upload.py script. For example, to do the locking sequence simple
type
```
$ ./upload.py < examples/lmx_lock.py
```

## Internals

You can find the internal of the python object [here]
(https://github.com/bkoppelmann/micropython/tree/b0d8c69e8fa030aa05168c5b6f820bab321caf6f/ports/arty)

- [SPI]
  (https://github.com/bkoppelmann/micropython/blob/b0d8c69e8fa030aa05168c5b6f820bab321caf6f/ports/arty/modpybspi.c)
- [PULPINO](https://github.com/bkoppelmann/micropython/blob/b0d8c69e8fa030aa05168c5b6f820bab321caf6f/ports/arty/modpybpulpino.c)
