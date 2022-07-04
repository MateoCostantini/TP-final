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
    parser.add_argument('-v', '--val', choices=[2, 4, 6, 8, 10], type=int, default=2, help='valores posibles')
    parser.add_argument('-p', '--point', help='puntajes', type=int)
    parser.add_argument('-n', '--name', help='nombre asociado a los puntajes y valores')
 # Parseo de argumentos
    arg = parser.parse_args() # arg contiene como atributos los parámetros ingresados
    print(f'Contenido del argumento val: {arg.val} (type: {type(arg.val)})')
    print(f'Contenido del argumento point: {arg.point} (type: {type(arg.point)})')
    print(f'Contenido del argumento name: {arg.name} (type: {type(arg.name)})')
    track = notes(fs)
    sound(track, fs)


if __name__ == "__main__":
    main()