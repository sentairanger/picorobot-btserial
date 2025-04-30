# Import necessary modules
from picozero import DigitalOutputDevice, PWMOutputDevice, LED
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# Motor pins
pin1 = DigitalOutputDevice(0)
pin2 = DigitalOutputDevice(1)
pin3 = DigitalOutputDevice(2)
pin4 = DigitalOutputDevice(3)
en1 = PWMOutputDevice(4)
en2 = PWMOutputDevice(5)
eye = LED(6)

eye.blink(n=4)
    

# Initialize motor state pins to zero for the pins that require it
motor_state = 0

# Define a callback function to handle received data
def on_rx(data):
    print("Data received: ", data)  # Print the received data
    global motor_state # Access the global variable led_state
    if data == b'forward\r\n':  # Check if the received data is "forward"
        pin1.value = 0
        pin2.value = not motor_state
        pin3.value = 0
        pin4.value = not motor_state
        motor_state = 1 - motor_state
    if data == b'backward\r\n':
        pin1.value = not motor_state
        pin2.value = 0
        pin3.value = not motor_state
        pin4.value = 0
        motor_state = 1 - motor_state
    if data == b'left\r\n':
        pin1.value = 0
        pin2.value = not motor_state
        pin3.value = not motor_state
        pin4.value = 0
        motor_state = 1 - motor_state
    if data == b'right\r\n':
        pin1.value = not motor_state
        pin2.value = 0
        pin3.value = 0
        pin4.value = not motor_state
        motor_state = 1 - motor_state
    if data == b'half\r\n':
        en1.value = 0.5
        en2.value = 0.5
    if data == b'full\r\n':
        en1.value = 1
        en2.value = 1

# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        sp.on_write(on_rx)  
