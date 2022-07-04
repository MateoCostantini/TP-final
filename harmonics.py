# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:22:33 2022

@author: Nusa
"""
import numpy as np
import matplotlib.pyplot as plt


def get_tone(harmonics_list, partiture, mods, fs): #4
    ts = 1/fs
    track = np.zeros(int((partiture[-1][0]+partiture[-1][2])/ts))
    print(len(track))
    for i in range(len(partiture)):
        t = np.arange(0, (len(mods[i]))/fs, ts)
        c = np.zeros(len(t))
        for k in range(len(harmonics_list)):
            note = harmonics_list[k][1]*np.sin(harmonics_list[k][0]*2*np.pi*partiture[i][1]*t)
            print(c)
            c += note
        note = c * mods[i]
        print("--")
        print(int(partiture[i][0]/ts) + len(note)-(int(partiture[i][0]/ts)))
        print(len(note))
        track[int(partiture[i][0]/ts):int(partiture[i][0]/ts) + len(note)] += track[int(partiture[i][0]/ts):int(partiture[i][0]/ts) + len(note)] + note
        print(track)
    track = track/np.max(abs(track))
    return track

