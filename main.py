# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:46:50 2022

@author: 54911
"""
import analyze_files
import module
import harmonics
import numpy as np
from scipy.io.wavfile import write
import argparse


def notes(fs, partiture_file, instrument_file):
    """
    The function first gives both the files to the function 
    get_instrument in analyze_files, which returns the harmonic_list
    and module_list which is then in turn given to get_partiture in 
    analyze_files that later returns partiture, which is given to 
    get_tone in harmonics, that returns the track.
    Parameters
    ----------
    fs : int
        Is the sample rate that is given by the person running
        the program
    partiture_file : file
        Is a file with all the specifications of the song, including
        the time each note starts, the note itself, and how long it
        has to play for
    instrument_file : file
        A file that contains the pianos infomration, including
        harmonics, and the attack constant and decay time that would
        be added to the different notes
    Returns
    -------
    track, which is a vector with all the notes of the song added 
    together
    """
    
    harmonics_list, module_list = analyze_files.get_instrument(instrument_file)
    partiture = analyze_files.get_partiture(partiture_file)
    track = harmonics.get_tone(harmonics_list, partiture, module_list, fs)
    return track


def sound(track, fs, out_file):
    """
    This function generates a .wav file with the given arguments
    
    Parameters
    ----------
    An array with all the notes of the song added together
   fs : int
       Is the sample rate that is given by the person running
       the program
   out_file : file.wav
       a .wav file that 'stores' the track which can then be used 
       to listen to the song in its entirety
   Returns
   -------
   None.
    """
    data =  2**15/np.max(abs(track)) * track
    write(out_file , fs, data.astype(np.int16))
    

def main():
    """
    This function was elaborated so that the code can be executed from the terminal which accepts different arguments and different songs.
    so that the sound of the final product changes according to the entered scores.

    Returns
    -------
    Track.

    """
    parser = argparse.ArgumentParser(description='Se ingresan el archivo de la partitura, el archivo del instrumento, el tiempo de muestreo, se elige el nombre del archivo wav')
    parser.add_argument('-p', '--partiture', help='Nombre del archivo de entrada que describe la partitura')
    parser.add_argument('-i', '--instrument', help='Nombre del archivo de entrada que describe un instrumento')
    parser.add_argument('-o', '--out', help='Nombre del archivo de salida (archivo WAVE a generar)')
    parser.add_argument('-f', '--frequency_lapse', choices=[8000, 9600, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000], type=int, default=48000, help='Frecuencia de muestreo. Una entre: 8000, 9600, 11025, 12000, 16000, 22050, 24000, 32000, 441000, 48000, 88200, 96000')
    arg = parser.parse_args()
    track = notes(arg.frequency_lapse, arg.partiture, arg.instrument)
    sound(track, arg.frequency_lapse, arg.out)
    return track


if __name__ == "__main__":
    main()