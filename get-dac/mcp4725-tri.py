import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 4.0           
signal_frequency = 5      
sampling_frequency = 1000 
vref = 5.0        

try:
    dac = mcp.MCP4725(dynamic_range=vref, address=0x61, verbose=True)

    t0 = time.time()

    while True:
        t = time.time() - t0
        norm_amp = sg.get_triangle_wave_amplitude(signal_frequency, t)
        voltage = norm_amp * amplitude
        dac.set_voltage(voltage, vref)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()