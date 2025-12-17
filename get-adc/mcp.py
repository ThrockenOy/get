import time
import matplotlib.pyplot as plt
from mcp3021_driver import MCP3021 

    
time_duration = 10
adc = MCP3021(3.189, verbose=False)


voltages = []
timestamps = []

try:
    start_time = time.time()
    while time.time() - start_time < MEASUREMENT_DURATION:
        voltage = adc.get_voltage()
        current_time = time.time() - start_time

        voltages.append(voltage)
        timestamps.append(current_time)
        time.sleep(0.1)

finally:
    adc.deinit()

plt.figure(figsize=(10, 5))
plt.plot(timestamps, voltages, marker='o', linestyle='-', color='blue')
plt.title("Напряжение на входе MCP3021")
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(voltages, bins=20, color='green', edgecolor='black')
plt.title("Распределение измеренных напряжений")
plt.xlabel("Напряжение, В")
plt.ylabel("Количество измерений")
plt.grid(axis='y')
plt.show()