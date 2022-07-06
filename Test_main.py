# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:56:29 2022

@author: Nusa
"""
from main import notes
import piano

def test_notes():
    fs = 44100
    partiture_file = open('partiture.txt', 'r')
    instrument_file = piano
    harmonics_list, module_list = [(1, 1),(2, 1), (3, 0), (4, 1)], [('LINEAR', 0.02), ('CONSTANT',), ('INVEXP', 0.06)]
    partiture = [(0, 261.626, 0.5), (0.5, 293.665, 0.5), (1, 329.628, 0.5), (1.2, 261.626, 0.7)]
    track = 86417
    partiture_file.close()
    assert notes(fs, partiture_file, instrument_file) == 86437, 'Not passed'
    
    