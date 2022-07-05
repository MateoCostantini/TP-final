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
    
    """
    harmonics_list, module_list = analyze_files.get_instrument(instrument_file)
    partiture = analyze_files.get_partiture(partiture_file)
    track = harmonics.get_tone(harmonics_list, partiture, module_list, fs)
    return track


def sound(track, fs, out_file):
    """
    
    """
    data =  2**15/np.max(abs(track)) * track
    write(out_file , fs, data.astype(np.int16))
    

def main():
    """
    

    Returns
    -------
    None.

    """
    parser = argparse.ArgumentParser(description='Descripción general')
    parser.add_argument('-p', '--partiture', help='Nombre del archivo de entrada que describe la partitura')
    parser.add_argument('-i', '--instrument', help='Nombre del archivo de entrada que describe un instrumento')
    parser.add_argument('-o', '--out', help='Nombre del archivo de salida (archivo WAVE a generar)')
    parser.add_argument('-f', '--frequency_lapse', choices=[8000, 9600, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000], type=int, default=48000, help='Frecuencia de muestreo. Una entre: 8000, 9600, 11025, 12000, 16000, 22050, 24000, 32000, 441000, 48000, 88200, 96000')
    arg = parser.parse_args()
    track = notes(arg.frequency_lapse, arg.partiture, arg.instrument)
    sound(track, arg.frequency_lapse, arg.out)


if __name__ == "__main__":
    main()