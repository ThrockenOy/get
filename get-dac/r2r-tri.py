import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2           
signal_frequency = 10     
sampling_frequency = 1000 

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], dynamic_range=3.3, verbose=False)
    
    while True:
        norm_amp = sg.get_triangle_wave_amplitude(signal_frequency, time.time())
        voltage = norm_amp * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()