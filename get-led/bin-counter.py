import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 23, 22, 24]

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
if GPIO.input(up):
    num =num+1
    print(num, dec2bin(num))
    time.sleep(sleep_time)    