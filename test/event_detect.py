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

IRQpin = 16;
OUTpin = 12;
toggle = False
BOUNCETIME = 1000   # microseconds

# handle the button event

def buttonEventHandler_falling (pin, timestamp):
    global toggle
    print(f'Pin = {pin:d}, timestamp = {timestamp:d}')
    if (toggle == True):
        # turn LED on
        GPIO.output(OUTpin,True)
        toggle = False
    else:
        # turn LED off
        GPIO.output(OUTpin, False)
        toggle = True

# main function
def main():
    GPIO.setmode(GPIO.BCM)

# GPIO IRQpin set up as input.
    GPIO.setup(IRQpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(OUTpin, GPIO.OUT, initial=GPIO.HIGH)
    
    print('Test add_event_detect without callback, check if event fired with event_detected function')
    GPIO.add_event_detect(IRQpin, GPIO.FALLING,  bouncetime=BOUNCETIME)
    print('loop with event_detected until button pressed')
    print()
    while GPIO.event_detected(IRQpin) == False:
        pass
    print('button pressed detected,  now remove event detection')
    GPIO.remove_event_detect(IRQpin)
    print()  
    
    print('Test wait_for_edge with timeout 10s')
    time.sleep(1)
    channel = GPIO.wait_for_edge(IRQpin, GPIO.RISING, bouncetime=BOUNCETIME, timeout=10000)
    if (channel == -1):
        print('wait_for_edge timeout')
    elif (channel == IRQpin):
        print('wait_for_edge fired')
    else:
        print(f'wait_for_edge returned None, Timeout!')
    
    print()
    print(f'Now starting add_event_detect with interrupt on falling edge with callback and bouncetime {BOUNCETIME:d} microseconds')
    GPIO.add_event_detect(IRQpin, GPIO.FALLING, callback=buttonEventHandler_falling, bouncetime=BOUNCETIME)
 
    try:  
        while True :
            time.sleep(1)
            
    except (Exception, KeyboardInterrupt):
        print('Interrupted')
        GPIO.remove_event_detect(IRQpin)
        GPIO.cleanup(IRQpin)  
        GPIO.cleanup(OUTpin)

if __name__=="__main__":
    main()