import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

up = 9
down = 10
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (up, GPIO.IN)
GPIO.setup (down, GPIO.IN)
num = 0



def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0,2
while True:
    num = int(input())

    if GPIO.input(up):
        if -1<num<254:
            num =num+1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        else:
            print('0')    

    if GPIO.input(down):
        if 0<num<255:
            num =num-1
            print(num, dec2bin(num))
            GPIO.output()
            time.sleep(sleep_time)  
        else:
            print('0')
    for i, pin in leds:
        GPIO.OUT(pin, int(dec2bin(num)[i]))