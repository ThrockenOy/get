
import time 
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

adc = R2R_ADC(dynamic_range = 3.3)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage = adc.get_sc_voltage()

        current_time = time.time() - start_time
        voltage_values.append(voltage)
        time_values.append(current_time)

    plot_voltage_vs_time(time_values, voltage_values, max_voltage = 3.3)
    plot_sampling_period_hist(time_values)
finally:
    adc.deinit()    