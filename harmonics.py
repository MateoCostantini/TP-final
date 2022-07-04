# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:47:43 2022

@author: 54911
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


# def final_partiture(notes, mods, partiture, ts):
#     final_notes = []
#     song_length = 0
#     for i in range(len(notes)):
#         for k in range(len(notes[i])):
#             song_length += 1
#     track = np.zeros(song_length)
#     for i in range(len(notes)):
#         print(len(notes))
#         print(len(mods))
#         print(len(notes[i]))
#         print(len(mods[i]))
#         final_note = notes[i] * mods[i]
#         final_notes.append(final_note)
#     for note in range(len(final_notes)):
#         track[int(partiture[note][0]/ts):int(partiture[note][0]/ts) + len(final_notes[note])] = track[int(partiture[note][0]/ts):int(partiture[note][0]/ts) + len(final_notes[note])] + final_notes[note]
#     track = track/np.max(abs(track))
#     return track

        