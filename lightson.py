#!/bin/python
import blinkt
import time

while True:
    for i in range(8):
        blinkt.set_pixel(i,250,80,250)
    blinkt.show()
    time.sleep(1)
    for i in range(8):
        blinkt.set_pixel(i,250,250,50)
    blinkt.show()
    time.sleep(1)
    
