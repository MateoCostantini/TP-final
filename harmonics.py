# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:47:43 2022

@author: 54911
"""
import numpy as np

def get_tone(harmonics_list, partiture, fs):
    harmonics = []
    notes = []
    ts = 1/fs
    for i in range(len(partiture)):
        t = np.arange(partiture[i][0], partiture[i][0]+partiture[i][2], ts)
        c = np.zeros(len(t))
        for k in range(len(harmonics_list)):
            note = harmonics_list[k][1]*np.sin(harmonics_list[k][0]*np.pi*partiture[i][1]*t)
            harmonics.append(note)
        for j in range(len(harmonics)):
            c += harmonics[j]
        harmonics = []
        notes.append(c)
    return notes