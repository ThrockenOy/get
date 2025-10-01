import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [22, 27, 17, 26, 25, 21, 20, 16]
GPIO.setup(pins, GPIO.OUT)

dynamic_range = 3.3


def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dunamic_range:.2f} В")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage/dynamic_range*255)

def number_to_dac(number):
    return [int(element) for element in bin(number)[2:].zfill(8)]
    for i in range (len(N)):
        GPIO.output(pins[i], number_to_dac(number)[i])
    print(number, number_to_dac(number))


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()


