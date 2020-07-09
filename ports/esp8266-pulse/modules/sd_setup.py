from machine import Pin, SPI
import sdcard
import os
import gc

os.mount(sdcard.SDCard(SPI(1), Pin(15)), '/sd')
gc.collect()
