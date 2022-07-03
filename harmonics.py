# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:47:43 2022

@author: 54911
"""
import numpy as np
import matplotlib.pyplot as plt


def get_tone(harmonics_list, partiture, fs): #4
    harmonics = []
    notes = []
    ts = 1/fs
    for i in range(len(partiture)):
        t = np.arange(0, partiture[i][2], ts)
        c = np.zeros(len(t))
        for k in range(len(harmonics_list)):
            note = harmonics_list[k][1]*np.sin(harmonics_list[k][0]*np.pi*partiture[i][1]*t)
            harmonics.append(note)
        for j in range(len(harmonics)):
            c += harmonics[j]
        harmonics = []
        notes.append(c)
    return notes


def final_partiture(notes, mods, partiture, ts):
    final_notes = []
    song_length = 0
    for i in range(len(notes)):
        for k in range(len(notes[i])):
            song_length += 1
    zeros = np.zeros(song_length)
    for i in range(len(notes)):
        print(len(notes[i]))
        print(len(mods[i]))
        final_note = notes[i] * mods[i]
        plt.plot(final_note)
        final_notes.append(final_note)
    for note in range(len(final_notes)):
        zeros[(partiture[note][0])/ts:(partiture[note][0] + partiture[notes][2])/ts] = zeros[(partiture[note][0])/ts:(partiture[note][0] + partiture[notes][2])/ts] + final_notes[note]
    return zeros

        