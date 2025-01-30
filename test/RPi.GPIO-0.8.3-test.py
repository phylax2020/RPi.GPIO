#!/usr/bin/env python
#
# RPi.GPIO add_event_detect test
##*************************************
## BCM pins
## btn_input : setup as input with internal pullup. Connected with push button to GND with 1K resistor in series.
## LED_output : connected to a LED with 470 Ohm resistor in series to GND. Toggles LED with every push button pressed.
##*************************************
#

import time
import RPi.GPIO as GPIO

btn_input = 16;
LED_output = 12;
toggle = False
bouncetime = 300

# handle the button event

def buttonEventHandler_falling (pin, timestamp):
    global toggle
    print(f'Pin = {pin:d}, timestamp = {timestamp:d}')
    if (toggle == True):
        # turn LED on
        GPIO.output(LED_output,True)
        toggle = False
    else:
        # turn LED off
        GPIO.output(LED_output, False)
        toggle = True

# main function
def main():
    GPIO.setmode(GPIO.BCM)

# GPIO btn_input set up as input.
    GPIO.setup(btn_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_output, GPIO.OUT)
    
    print('Test add_event_detect without callback, check if event fired with event_detected function')
    GPIO.add_event_detect(btn_input, GPIO.FALLING)
    print('loop with event_detected until button pressed')
    while GPIO.event_detected(btn_input) == False:
        pass
    print('button pressed detected,  now remove event detection')
    GPIO.remove_event_detect(btn_input)
    print()  
    
    print('Test wait_for_edge with timeout 10s')
    channel = GPIO.wait_for_edge(btn_input, GPIO.RISING, timeout=10000)
    if (channel == -1):
        print('wait_for_edge timeout')
    elif (channel == btn_input):
       print('wait_for_edge fired')
    else:
        print(f'wait_for_edge returned {channel:d}')
    
    print()
    print(f'Now starting add_event_detect with interrupt on falling edge with callback and bouncetime {bouncetime:d} ms')
    GPIO.add_event_detect(btn_input, GPIO.FALLING, callback=buttonEventHandler_falling, bouncetime=bouncetime)
 
    try:  
        while True :
            time.sleep(1)
            
    except (Exception, KeyboardInterrupt):
        print('Interrupted')
        GPIO.remove_event_detect(btn_input)
        GPIO.cleanup(btn_input)  
        GPIO.cleanup(LED_output)

if __name__=="__main__":
    main()