import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()





    def set_number(self, number):
        max_num = (1 << len(self.gpio_bits)) - 1
        if number < 0 or number > max_num:
            raise ValueError(f"Не входит в диапазон")

 
        bits = [int(b) for b in bin(number)[2:].zfill(len(self.gpio_bits))]

        for pin, bit in zip(self.gpio_bits, bits):
            GPIO.output(pin, GPIO.HIGH if bit else GPIO.LOW)

        if self.verbose:
            print(f"Число на вход ЦАП: {number}, Биты: {bits}")


    def set_voltage(self, voltage):

        if voltage < 0 or voltage > self.dynamic_range:
            if self.verbose:
                print(f" Напряжение {voltage:.2f} В выходит за диапазон 0-{self.dynamic_range:.2f} В. Устанавливаем 0 В.")
            voltage = 0.0

        max_num = (1 << len(self.gpio_bits)) - 1
        number = int(round((voltage / self.dynamic_range) * max_num))

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