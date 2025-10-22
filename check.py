import RPi.GPIO as GPIO
import time

bits = [26, 20, 19, 16, 13, 12, 25, 11]
GPIO.setmode(GPIO.BCM)
GPIO.setup(bits, GPIO.OUT, initial=0)
GPIO.output(bits, [1, 1, 1, 1, 1, 1, 1, 1])

print("апвоыш")
GPIO.cleanup()