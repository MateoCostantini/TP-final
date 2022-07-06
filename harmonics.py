# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:47:43 2022

@author: 54911
"""
import numpy as np
import module


def get_tone(harmonics_list, partiture, module_list, fs): #4
    """
    This function creates notes_duration, which using the for, is a 
   list that then houses the time it takes to play the song with 
   all the notes that are given. It then creates 'track' which is a 
   vector with the same duration as the song, but with its value 
   being 0, then the for then adds the notes onto track, and given 
   that track is 0, the track then become the notes added onto the 
   vector which then can be used to play the song.
   Parameters
   ----------
   harmonics_list : tuple
       the list containing the harmonics of the different notes
   partiture : file
       contains the notes of the song that will be played
   module_list : tuple
       a list containing the attack, constant and decay when using a piano
   fs : int
       it's the showing frequency
   Returns
   -------
   track, which is the song in its entirety
    """
    ts = 1/fs
    notes_duration = []
    for i in range(len(partiture)):
        length = (partiture[i][0] + partiture[i][2])/ts
        notes_duration.append(length)
    track = np.zeros(int(max(notes_duration) + (module_list[2][1])*fs)+1)
    for sound in range(len(partiture)):
        mod = module.get_mod(module_list, partiture, fs, sound)
        t = np.arange(0, (len(mod))/fs, ts)
        c = np.zeros(len(t))
        for k in range(len(harmonics_list)):
            note = harmonics_list[k][1]*np.sin(harmonics_list[k][0]*2*np.pi*partiture[sound][1]*t)
            c += note
        note_length = min([len(c)-1, len(mod)-1])
        note = c[:note_length] * mod[:note_length]
        track[int(partiture[sound][0]/ts):int(partiture[sound][0]/ts) + len(note)] = track[int(partiture[sound][0]/ts):int(partiture[sound][0]/ts) + len(note)] + note
    track = track/np.max(abs(track))
    return track
