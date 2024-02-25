from scipy.io import wavfile as wav
from IPython.display import Audio

def write(name, data):
    wav.write(name, fs, data.astype('int16'))

def play_file(name):
    print('\n'+name+":")
    display(Audio(filename=name))