# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:19:08 2022

@author: 54911
"""
import notes

def get_instrument(): #2
    """
    
    """
    harmonics_list = []
    module_list = []
    with open("piano.txt", "r") as f:
        line = f.readline()
        line = int(line)
        for i in range(line):
            line = f.readline()
            harmonic = line.split(" ")
            harmonic[0], harmonic[1] = int(harmonic[0]), float(harmonic[1])
            harmonic = tuple(harmonic)
            harmonics_list.append(harmonic)
        for i in range(3):
            line = f.readline()
            module = (line.rstrip()).split(" ")
            for k in range(1, len(module)):
                module[k] = float(module[k])
            module = tuple(module)
            module_list.append(module)
    return harmonics_list, module_list


def get_partiture(): #4
    """
    
    """
    partiture= []
    with open("partiture.txt", "r") as f:
        for line in f:
            note = (line.rstrip()).split(" ")
            for i in range(len(notes.notes_mapping)):
                if note[1] == notes.notes_mapping[i][0]:
                    note[1] = notes.notes_mapping[i][1]
                    break
            note[0], note[2] = float(note[0]), float(note[2])
            note = tuple(note)
            partiture.append(note)
    return partiture