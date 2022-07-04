# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:46:50 2022

@author: 54911
"""
import analyze_files
import module
import harmonics
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
import argparse


fs = 44100
def notes(fs):
    """
    
    """
    harmonics_list, module_list = analyze_files.get_instrument()
    partiture = analyze_files.get_partiture()
    mods = module.get_mod(module_list, partiture, fs)
    track = harmonics.get_tone(harmonics_list, partiture, mods, fs)
    # track = harmonics.final_partiture(notes, mods, partiture, ts)
    plt.plot(track)
    return track


def sound(track, fs):
    """
    
    """
    data =  2**15/np.max(abs(track)) * track
    write("audio.wav", fs, data.astype(np.int16))
    

def main():
    """
    

    Returns
    -------
    None.

    """
    # Inicializar objeto argparse
    parser = argparse.ArgumentParser(description='Descripción general')
 # Agregar argumentos (flag, --atributo, opciones..., help)
    parser.add_argument('-f', '--frequency_lapse', choices=[8000, 9600, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000], type=int, default=48000, help='frecuencias de muestreo posibles')
    parser.add_argument('-p', '--partiture', help='archivo de partiture (.txt)', type=str)
    parser.add_argument('-i', '--instrument', help='archivo del instrumento (.txt)', type=str)
 # Parseo de argumentos
    arg = parser.parse_args() # arg contiene como atributos los parámetros ingresados
    print(f'Contenido del argumento frequency_lapse: {arg.frequency_lapse} (type: {type(arg.frequency_lapse)})')
    print(f'Contenido del argumento partiture: {arg.partiture} (type: {type(arg.partiture)})')
    print(f'Contenido del argumento instrument: {arg.instrument} (type: {type(arg.instrument)})')
    track = notes(fs)
    sound(track, fs)


if __name__ == "__main__":
    main()