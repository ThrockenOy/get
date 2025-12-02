import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2           
signal_frequency = 10     
sampling_frequency = 1000 

try:
    dac = pwm.PWM_DAC(gpio_pin=12, pwm_frequency=500, dynamic_range=3.3, verbose=True)


    while True:
        norm_amp = sg.get_triangle_wave_amplitude(signal_frequency, time.time())
        voltage = norm_amp * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()