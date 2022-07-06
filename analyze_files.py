# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:19:08 2022

@author: 54911
"""
import notes

def get_instrument(instrument_file): #2
    """
    This function reads piano.txt and generates a list with the data of every line of the archive. The function
    recives the information of the instrument as instrument_file.
    
    
    This function returns two lists, harmonics_list and module_list
    
        harmonics_list: Is a list with a tuple inside, that contains all the harmonics of the song
        module_list: Is a list with a tuple inside that has all the modulatings, those are: the attack, constant, and dacay
    """
    harmonics_list = []
    module_list = []
    with open(instrument_file, "r") as f:
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


def get_partiture(partiture_file): #4
    """
    gets the notes from the song that are going to be played, and
    filters them depending if they are playable by the xylophone or 
    not
    Parameters
    ----------
    partiture_file : file
        is a file that contains the start and time played of every 
        note and every note that the song has
    Returns
    -------
    partiture, which is a list containing all the notes from the song
    """
    partiture= []
    with open(partiture_file, "r") as f:
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