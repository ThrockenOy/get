import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    y = np.sin(2 * np.pi * freq * t)
    y += 1
    y /= 2
    return y

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)

def get_triangle_wave_amplitude(freq, t):
    period = 1 / freq
    x = t % period
    value = 2 * (x / period)
    if value > 1:
        value = 2 - value
    return value
