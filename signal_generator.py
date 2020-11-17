import random

import numpy as np
from scipy import signal
from matplotlib import pyplot

from constants import SAMPLE_LENGHT
from utils import save_signal


def harmonic_signal_generator(amplitude, sample_rate, wave_freq, offset, sample_lenght):

    t_vector = np.linspace(0, 1, sample_lenght)
    res = amplitude * np.sin((2*np.pi*t_vector*wave_freq)/sample_rate + offset)
    pyplot.plot(t_vector, res)
    pyplot.xlim(0, 0.1)
    pyplot.show()

    return res


def triangle_sawtooth_signal_generator(sample_length, wave_freq, signal_type, amplitude):

    t_vector = np.linspace(0, 1, sample_length)
    res = amplitude * signal.sawtooth(2 * np.pi * wave_freq * t_vector, signal_type)
    pyplot.plot(t_vector, res)
    pyplot.xlim(0, 0.1)
    pyplot.show()

    return res


def noise_generator(amplitude, sample_length, min_value, max_value):

    n_vector = np.array([random.uniform(min_value, max_value) for _ in range(sample_length)])
    res = amplitude * n_vector
    pyplot.plot(n_vector, res)
    pyplot.ylim(0, 1.5)
    pyplot.xlim(min_value, max_value)
    pyplot.show()

    return res


def square_signal_generator(sample_length, frequency, amplitude):
    t_vector = np.linspace(0, 1, sample_length)
    res = amplitude * signal.square(2*np.pi*frequency*t_vector, duty=0.5)
    pyplot.plot(t_vector, res)
    pyplot.xlim(0, 0.1)
    pyplot.show()

    return res


def impulse_duty_signal_generator(sample_length, wave_freq, offset_duty, amplitude):

    t_vector = np.linspace(0, 1, sample_length, endpoint=False)
    duty = np.sin(2 * np.pi * t_vector + offset_duty)
    res = amplitude * signal.square(2 * np.pi * t_vector * wave_freq, duty=(duty + 1)/2)
    pyplot.plot(t_vector, res)
    pyplot.ylim(-1.5, 1.5)
    pyplot.xlim(0, 0.5)
    pyplot.show()

    return res


def amplitude_modulation_generator(sig_type, amp, freq, sample_length, lfo):
    signal_output = 0
    t_vector = np.linspace(0, 1, sample_length)
    if sig_type == "sin_":
        signal_output = (amp + amp * lfo) * np.sin(2 * np.pi * freq * t_vector)
    elif sig_type == "sq_":
        signal_output = (amp + amp * lfo) * signal.square(2 * np.pi * freq * t_vector)
    elif sig_type == "tr_":
        signal_output = (amp + amp * lfo) * signal.sawtooth(2 * np.pi * freq * t_vector, width=0.5)
    elif sig_type == "st_":
        signal_output = (amp + amp * lfo) * signal.sawtooth(2 * np.pi * freq * t_vector)
    elif sig_type == "noise_":
        signal_output = (amp + amp * lfo) * np.random.random_sample(len(t_vector))

    pyplot.plot(t_vector, signal_output)
    pyplot.xlim(0, 0.5)
    pyplot.show()

    return signal_output


def frequency_modulation_generator(sig_type, amp, freq, sampling_freq, sample_length, lfo, duty=0.5):
    signal_output = np.zeros_like(lfo)
    phi = 0
    t_vector = np.linspace(0, 1, sample_length)
    if sig_type == "sin_":
        for i in range(len(t_vector)):
            phi += 2.0 * np.pi * (freq + freq * lfo[i]) / sampling_freq
            signal_output[i] = amp * np.sin(phi)
    elif sig_type == "sq_":
        for i in range(len(t_vector)):
            phi += 2.0 * np.pi * (freq + freq * lfo[i]) / sampling_freq
            if (phi % (2.0 * np.pi)) / (2.0 * np.pi) < duty:
                signal_output[i] = amp * 1
            else:
                signal_output[i] = amp * (-1)
    elif sig_type == "tr_":
        for i in range(len(t_vector)):
            phi += 2.0 * np.pi * (freq + freq * lfo[i]) / sampling_freq
            signal_output[i] = amp * signal.sawtooth(phi, width=0.5)
    elif sig_type == "st_":
        for i in range(len(t_vector)):
            phi += 2.0 * np.pi * (freq + freq * lfo[i]) / sampling_freq
            signal_output[i] = amp * signal.sawtooth(phi)

    pyplot.plot(t_vector, signal_output)

    pyplot.xlim(0, 0.5)
    pyplot.show()

    return signal_output


def combine_two_signals(first_signal, second_signal):
    res = first_signal + second_signal
    save_signal(res, SAMPLE_LENGHT, 'combine_')
    return True