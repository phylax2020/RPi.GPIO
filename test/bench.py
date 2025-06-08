#!/usr/bin/env python
"""
bench.py
2020-11-18
Public Domain

http://abyz.me.uk/lg/py_lgpio.html

./bench.py
"""
import time
import lgpio
import RPi.GPIO as GPIO

print(GPIO.RPI_INFO)

OUT=12
LOOPS=100000

h = lgpio.gpiochip_open(0)

lgpio.gpio_claim_output(h, OUT)

t0 = time.time()

for i in range(LOOPS):
   lgpio.gpio_write(h, OUT, 0)
   lgpio.gpio_write(h, OUT, 1)

t1 = time.time()

lgpio.gpiochip_close(h)

print("lgpio:    {:.0f} toggles per second".format(LOOPS/(t1-t0)))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OUT, GPIO.OUT)

t0 = time.time()

for i in range(0,LOOPS):
    GPIO.output(OUT, GPIO.HIGH)
    GPIO.output(OUT, GPIO.LOW)
    
t1 = time.time()
print("RPi.GPIO: {:.0f} toggles per second".format(LOOPS/(t1-t0)))