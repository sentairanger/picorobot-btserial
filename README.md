# picorobot-btserial
This project uses the Serial Bluetooth Terminal App to control a Pico W robot

## Getting Started

First you'll need the Serial Bluetooth Terminal App on Android to control the robot. You will also need a Pico W and a robot. You can use any robot chassis. Be sure to have the latest version of MicroPython and please clone the picozero library from [here](https://github.com/RaspberryPiFoundation/picozero). Copy the `picozero.py` file into the Pico W. The normal way to install picozero doesn't work. Copy these other files from the repo into the Pico W and then rename the `robot_uart.py` file into `main.py`. After that you should be able to move the robot without programming it.
