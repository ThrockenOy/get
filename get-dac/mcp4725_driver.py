import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        
        self.verbose = verbose
        self.dynamic_range = dynamic_range


    def set_voltage(self, voltage, vref):
        if voltage < 0 or voltage > self.dynamic_range:
            if self.verbose:
                print(f" Напряжение {voltage:.2f} В выходит за диапазон 0-{self.dynamic_range:.2f} В. Устанавливаем 0 В.")
            voltage = 0.0

        value = int((voltage / vref) * 4095)

        command_byte = 0xC2
        high_byte = (value >> 4) & 0xFF
        low_byte = (value & 0x0F) <<4

        self.bus.write_i2c_block_data(self.address, command_byte, [high_byte, low_byte])

        print(f"Число: {value}")
        print(f"Данные, отправленные по I2C: {[hex(b) for b in [command_byte, high_byte, low_byte]]}")


    def deinit(self):
        self.bus.close()


if __name__ == "__main__":
    vref = 3.3
    try:
        dac = MCP4725(dynamic_range = 5.0, address = 0x61, verbose=True)
        while True:
            voltage = float(input("Введите напряжение: "))
            dac.set_voltage(voltage, vref)
    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()