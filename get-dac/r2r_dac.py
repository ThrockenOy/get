import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)


    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()


    def set_number(self, number):
        number = int(number)  
        if not (0 <= number <= 255):
            print(f"Число {number} выходит за диапазон 0-255. Устанавливаем 0.")
            number = 0

        bits = [int(b) for b in bin(number)[2:].zfill(8)]
        for i, pin in enumerate(self.gpio_bits):
            GPIO.output(pin, bits[i])
        if self.verbose:
            print(f"Число на вход ЦАП: {number}, Биты: {bits}")
            print(f"Число: {number}, Биты: {bits}")




    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            number = 0
        else:
            number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()






'''
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

class R2R_DAC:
    def __init__(self, pins, dynamic_range):
        self.pins = pins
        self.dynamic_range = dynamic_range

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pins, GPIO.OUT)

    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            return 0
        return int(voltage / self.dynamic_range * 255)

    def number_to_dac(self, number):
        pins = [int(element) for element in bin(number)[2:].zfill(8)]
        return pins

    def output_voltage(self,voltage):
        try:
            while True:
                try:
                    voltage = float(input("Введите напряжение в Вольтах: "))
                    number = self.voltage_to_number(voltage)
                    pins = self.number_to_dac(number)
                    for i in range(len(self.pins)):
                        GPIO.output(self.pins[i], pins[i])
                    print("Число на вход ЦАП:", number, "Биты:", pins)

                except ValueError:
                    print("Вы ввели не число. Попробуйте ещё раз\n")

        finally:
            GPIO.output(self.pins, 0)
            GPIO.cleanup()
    def deinit(self):
        GPIO.output(self.pins, 0)
        GPIO.cleanup()        



if __name__ == "__main__":
    
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183)
    try:
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.output_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
'''