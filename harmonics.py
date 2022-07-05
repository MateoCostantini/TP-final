# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:47:43 2022

@author: 54911
"""
import numpy as np


def get_tone(harmonics_list, partiture, mods, module_list, fs): #4
    ts = 1/fs
    notes_duration = []
    for i in range(len(partiture)):
        length = (partiture[i][0] + partiture[i][2])/ts
        notes_duration.append(length)
    track = np.zeros(int(max(notes_duration) + (module_list[2][1])*fs)+1) #int((partiture[-1][0]+partiture[-1][2])/ts)
    for i in range(len(partiture)):
        t = np.arange(0, (len(mods[i]))/fs, ts)
        c = np.zeros(len(t))
        for k in range(len(harmonics_list)):
            note = harmonics_list[k][1]*np.sin(harmonics_list[k][0]*2*np.pi*partiture[i][1]*t)
            c += note
        note_length = min([len(c)-1, len(mods[i])-1])
        note = c[:note_length] * mods[i][:note_length]
        track[int(partiture[i][0]/ts):int(partiture[i][0]/ts) + len(note)] = track[int(partiture[i][0]/ts):int(partiture[i][0]/ts) + len(note)] + note
    track = track/np.max(abs(track))
    return track
