# RPi.GPIO
RPi.GPIO wrapper for WiringPi supporting RPi 5B, RPi Zero W, RPi Zero 2W, RPi 3B,4B.

This repository is the continuation of Ben Croston's RPi.GPIO, because it seems that there are no plans 
to update the library to support RPi 5 and newer devices like RPi 500.

Thanks to the developers of WiringPi, who did a lot of work to support all Raspberry Pi boards now including RPi 5. The library controls the GPIO pins by directly accessing the hardware registers especially also including the RP1 chip registers. This enables the highest possible performance for GPIO operations. RPi.GPIO refers to the WiringPi Library and uses its functions so that they comply with the existing Python API.

![image](https://github.com/user-attachments/assets/0c0b5f5a-1047-423f-b89b-8c76ebf69edf)

Note that this module is unsuitable for real-time or timing critical applications.  This is because you
can not predict when Python will be busy garbage collecting.  It also runs under the Linux kernel which
is not suitable for real time applications - it is multitasking O/S and another process may be given
priority over the CPU, causing jitter in your program.  If you are after true real-time performance and
predictability, buy yourself an Arduino http://www.arduino.cc !

Although hardware PWM is not available yet, software PWM is available to use on all channels.

For examples and documentation, visit http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

