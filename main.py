import numpy as np
from matplotlib import pyplot

from constants import AMPLITUDE, SAMPLE_RATE, WAVE_FREQ, OFFSET, SAMPLE_LENGHT, SAMPLE_LENGHT_TR, WAVE_FREQ_TR, \
    SIGNAL_TYPE_TR, SIGNAL_TYPE_NAME_SIN, SIGNAL_TYPE_NAME_TR, SIGNAL_TYPE_ST, WAVE_FREQ_ST, SAMPLE_LENGHT_ST, \
    SIGNAL_TYPE_NAME_ST, MAX_VALUE, MIN_VALUE, SAMPLE_LENGHT_NOISE, AMPLITUDE_NOISE, SIGNAL_TYPE_NAME_NOISE, \
    SAMPLE_LENGHT_DUTY, WAVE_FREQ_DUTY, OFFSET_DUTY, SIGNAL_TYPE_NAME_DUTY, SIGNAL_TYPE_NAME_SQUARE, \
    SAMPLE_LENGHT_SQUARE, WAVE_FREQ_SQ, AMPLITUDE_SQ
from signal_generator import harmonic_signal_generator, triangle_sawtooth_signal_generator, noise_generator, \
    impulse_duty_signal_generator, square_signal_generator, combine_two_signals, amplitude_modulation_generator, \
    frequency_modulation_generator
from utils import save_signal

if __name__ == '__main__':
    message = ''
    signal = 0
    signal_sq = 0
    signal_tr = 0
    signal_st = 0
    noise = 0
    duty = 0
    while message != '0':
        message = input(
            "enter 1 to generate new signal, "
            "enter 2 to combine signals, "
            "enter 3 to modulate signal"
            "enter 0 to exit: ")
        if message == '1':
            amplitude = float(input("amplitude: "))
            frequency = float(input("frequency: "))
            sig_type = input("signal type: ")
            if sig_type == SIGNAL_TYPE_NAME_SQUARE:
                duty = float(input("duty: "))
                signal_sq = square_signal_generator(SAMPLE_LENGHT_SQUARE, frequency, amplitude)
                save_signal(signal_sq, SAMPLE_LENGHT_SQUARE, sig_type)
            if sig_type == SIGNAL_TYPE_NAME_SIN:
                signal = harmonic_signal_generator(amplitude, SAMPLE_RATE, frequency, OFFSET, SAMPLE_LENGHT)
                save_signal(signal, SAMPLE_LENGHT, sig_type)
            if sig_type == SIGNAL_TYPE_NAME_TR:
                signal_tr = triangle_sawtooth_signal_generator(SAMPLE_LENGHT_TR, frequency, SIGNAL_TYPE_TR, amplitude)
                save_signal(signal_tr, SAMPLE_LENGHT_TR, sig_type)
            if sig_type == SIGNAL_TYPE_NAME_ST:
                signal_st = triangle_sawtooth_signal_generator(SAMPLE_LENGHT_ST, frequency, SIGNAL_TYPE_ST, amplitude)
                save_signal(signal_st, SAMPLE_LENGHT_ST, sig_type)
            if sig_type == SIGNAL_TYPE_NAME_NOISE:
                noise = noise_generator(AMPLITUDE_NOISE, SAMPLE_LENGHT_NOISE, MIN_VALUE, MAX_VALUE)
                save_signal(noise, SAMPLE_LENGHT_NOISE, sig_type)
            if sig_type == SIGNAL_TYPE_NAME_DUTY:
                duty = impulse_duty_signal_generator(SAMPLE_LENGHT_DUTY, frequency, OFFSET_DUTY, amplitude)
                save_signal(duty, SAMPLE_LENGHT_DUTY, sig_type)
        if message == '2':
            first_signal_type = input("1st signal' type: ")
            second_signal_type = input("2nd signal' type: ")
            first_signal = 0
            second_signal = 0
            if first_signal_type == SIGNAL_TYPE_NAME_SIN:
                first_signal = signal
            elif first_signal_type == SIGNAL_TYPE_NAME_SQUARE:
                first_signal = signal_sq
            elif first_signal_type == SIGNAL_TYPE_NAME_ST:
                first_signal = signal_st
            elif first_signal_type == SIGNAL_TYPE_NAME_TR:
                first_signal = signal_tr
            elif first_signal_type == SIGNAL_TYPE_NAME_NOISE:
                first_signal = noise
            elif first_signal_type == SIGNAL_TYPE_NAME_DUTY:
                first_signal = duty

            if second_signal_type == SIGNAL_TYPE_NAME_SIN:
                second_signal = signal
            elif second_signal_type == SIGNAL_TYPE_NAME_SQUARE:
                second_signal = signal_sq
            elif second_signal_type == SIGNAL_TYPE_NAME_ST:
                second_signal = signal_st
            elif second_signal_type == SIGNAL_TYPE_NAME_TR:
                second_signal = signal_tr
            elif first_signal_type == SIGNAL_TYPE_NAME_NOISE:
                second_signal = noise
            elif first_signal_type == SIGNAL_TYPE_NAME_DUTY:
                second_signal = duty

            combine_two_signals(first_signal, second_signal)

        if message == '3':
            new_signal = 0
            modulate_signal = 0
            lfo = 0
            old_signal = input('Enter a signal type for an old signal: ')
            if old_signal == SIGNAL_TYPE_NAME_SIN:
                lfo = signal
            elif old_signal == SIGNAL_TYPE_NAME_SQUARE:
                lfo = signal_sq
            elif old_signal == SIGNAL_TYPE_NAME_ST:
                lfo = signal_st
            elif old_signal == SIGNAL_TYPE_NAME_TR:
                lfo = signal_tr
            elif old_signal == SIGNAL_TYPE_NAME_NOISE:
                lfo = noise
            elif old_signal == SIGNAL_TYPE_NAME_DUTY:
                lfo = duty
            amplitude = float(input("new amplitude: "))
            frequency = float(input("new frequency: "))
            sig_type = input("new signal type: ")
            if sig_type == SIGNAL_TYPE_NAME_SQUARE:
                duty = float(input("new duty: "))
                new_signal = square_signal_generator(SAMPLE_LENGHT_SQUARE, frequency, amplitude)
            if sig_type == SIGNAL_TYPE_NAME_SIN:
                new_signal = harmonic_signal_generator(amplitude, SAMPLE_RATE, frequency, OFFSET, SAMPLE_LENGHT)
            if sig_type == SIGNAL_TYPE_NAME_TR:
                new_signal = triangle_sawtooth_signal_generator(SAMPLE_LENGHT_TR, frequency, SIGNAL_TYPE_TR, amplitude)
            if sig_type == SIGNAL_TYPE_NAME_ST:
                new_signal = triangle_sawtooth_signal_generator(SAMPLE_LENGHT_ST, frequency, SIGNAL_TYPE_ST, amplitude)
            if sig_type == SIGNAL_TYPE_NAME_NOISE:
                new_signal = noise_generator(AMPLITUDE_NOISE, SAMPLE_LENGHT_NOISE, MIN_VALUE, MAX_VALUE)
            if sig_type == SIGNAL_TYPE_NAME_DUTY:
                new_signal = impulse_duty_signal_generator(SAMPLE_LENGHT_DUTY, frequency, OFFSET_DUTY, amplitude)

            param = input('Amplitude/frequency: ')
            if param == 'a':
                modulate_signal = amplitude_modulation_generator(sig_type, amplitude, frequency, SAMPLE_LENGHT, lfo)
                save_signal(modulate_signal, SAMPLE_LENGHT, 'amplitude')
            elif param == 'f':
                modulate_signal = frequency_modulation_generator(sig_type, amplitude, frequency, SAMPLE_LENGHT, SAMPLE_LENGHT, lfo, duty=0.5)
                save_signal(modulate_signal, SAMPLE_LENGHT, 'frequency')
