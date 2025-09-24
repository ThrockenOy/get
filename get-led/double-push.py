import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

up = 9
down = 10
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (up, GPIO.IN)
GPIO.setup (down, GPIO.IN)
num = 0

GPIO.output(leds, 0)


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2


while True:

    if GPIO.input(up):
        if num<255:
            num = num + 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        else:
            num = 0   

    if GPIO.input(down):
        if 0<num:
            num = num - 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)  
        else:       
            num = 0 
    if GPIO.input(down) and GPIO.input(up):
        num = 255       
        time.sleep(sleep_time)  
    for i in range (len(leds)):
        GPIO.output(leds[i], dec2bin(num)[i])