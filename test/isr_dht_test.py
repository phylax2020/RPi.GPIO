#!/usr/bin/env python
#
# RPi.GPIO add_event_detect test
##*************************************
## BCM pins
## IRQpin : setup as input with internal pullup. Connected with push button to GND with 1K resistor in series.
## OUTpin : connected to a LED with 470 Ohm resistor in series to GND. Toggles LED with every push button pressed.
##*************************************
#

import time
import RPi.GPIO as GPIO

DATA = 17
ticks = 0
last_timestamp = time.monotonic() * 1000000

# handle the button event

def rising_edge (pin, timestamp):
    global ticks, last_timestamp
    diff = timestamp - last_timestamp
    last_timestamp = timestamp
#    print(f'Pin = {pin:d}, timediff = {diff:f}')
    ticks = ticks + 1

# main function
def main():
    global ticks, last_timestamp
    GPIO.setmode(GPIO.BCM)

    print(f'Now starting add_event_detect with interrupt on rising edge with callback count interrupts')
 
    try:  
        while True :
            ticks = 0

            GPIO.setup(DATA, GPIO.OUT, initial=GPIO.HIGH )
            time.sleep( 0.5 )       # stay high about 0.5s
            GPIO.output(DATA, False) 
            time.sleep(0.001)
            last_timestamp = time.monotonic() * 1000000
#            GPIO.setup(DATA, GPIO.IN)
            GPIO.add_event_detect(DATA, GPIO.RISING, callback=rising_edge, bouncetime=0)
           
            time.sleep(1)
            print(f"DHT ticks = {ticks:d}")
            GPIO.remove_event_detect(DATA)
            
            time.sleep(0.5)
            
    except (Exception, KeyboardInterrupt):
        print('Interrupted')
        GPIO.remove_event_detect(DATA)
        GPIO.cleanup(DATA)

if __name__=="__main__":
    main()