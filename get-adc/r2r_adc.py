import RPi.GPIO as GPIO
import time 

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()  

    def number_to_dac(self, number):
        pins = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, pins)
        

    def sequental_counting_adc(self):
        max_value = 255
        for count in range(256):
            self.number_to_dac(count) #count -- текущий цифровой код (0, 255), подаем текущение значение на цап

            time.sleep(self.compare_time)

            comp_output = GPIO.input(self.comp_gpio) # читаем выход компаратора

            #print("Счет:", count, "Компаратор:", comp_output)

            if comp_output == 1: #то есть напр на цап превысило входное напряжение ацп
                return count

        return max_value

    def get_sc_voltage(self):
        return self.sequental_counting_adc()/255*self.dynamic_range #вольт


if __name__ == "__main__":

    adc = R2R_ADC(3.189)    

    try:
        while True:
            voltage = adc.get_sc_voltage()
            print("Напряжение:", voltage)

    finally:
        adc.deinit()
