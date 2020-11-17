from scipy.io.wavfile import write

from constants import DIR


def save_signal(sig, sample_lenght, sig_type):
    filename = DIR + sig_type + 'signal.wav'
    write(filename, sample_lenght, sig)
    return True
