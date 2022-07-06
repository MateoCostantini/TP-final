# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:56:29 2022

@author: Nusa
"""
from main import notes
import piano
import analyze_files
import harmonics
from harmonics import get_tone

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
        Is the showing frequency that is given by the person running
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


def test_notes():
    fs = 44100
    partiture_file = open('partiture.txt', 'r')
    instrument_file = piano
    harmonics_list, module_list = [(1, 1),(2, 1), (3, 0), (4, 1)], [('LINEAR', 0.02), ('CONSTANT'), ('INVEXP', 0.06)]
    partiture = [(0, 261.626, 0.5), (0.5, 293.665, 0.5), (1, 329.628, 0.5), (1.2, 261.626, 0.7)]
    
    partiture_file.close()
    assert notes(fs, partiture_file, instrument_file) == 86437, 'Not passed'
    
    