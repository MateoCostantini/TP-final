# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:12:18 2022

@author: 54911
"""
import functions
import harmonics
import numpy as np


def get_func(param, duration, fs):#1
    """
    This function allowes the user to choose between the module functions, CONSTANT, LINEAR, TRI,
    INVLINEAR, between others. Those then are used to generate the shape of the attack, sustain and decay.
    
    Parameters:
        param: A list that contains the type of function ans it's parameters
        duration: The duration of the function
        fs: Is the sample rate that is measured in Hz, given by the person running the program
        
    Returns: An array with the shape chosen.
    """
    ts = 1/fs
    t = np.arange(0, duration , ts)

    if param[0] == "CONSTANT":
        array = functions.CONSTANT(t)
    elif param[0] == "LINEAR":
        array = functions.LINEAR(t, param[1])
    elif param[0] == "INVLINEAR":
        array = functions.INVLINEAR(t, param[1])
    elif param[0] == "SIN":
        array = functions.SIN(t, param[1], param[2])
    elif param[0] == "EXP":
        array = functions.EXP(t, param[1])
    elif param[0] == "INVEXP":
        array = functions.INVEXP(t, param[1])
    elif param[0] == "QUARTCOS":
        array = functions.QUARTCOS(t, param[1])
    elif param[0] == "QUARTSIN":
        array = functions.QUARTSIN(t, param[1])
    elif param[0] == "HALFCOS":
        array = functions.HALFCOS(t, param[1])
    elif param[0] == "HALFSIN":
        array = functions.HALFSIN(t, param[1])
    elif param[0] == "LOG":
        array = functions.LOG(t, param[1])
    elif param[0] == "INVLOG":
        array = functions.INVLOG(t, param[1], ts)
    elif param[0] == "TRI":
        array = functions.TRI(t, param[1], param[2], param[3], ts)
    return array


def get_mod(module_list, partiture, fs, note):#2
    """
    Parameters: module_list, partiture, fs and the note
        module_list: Is a list with all the modules of the function get_instrument. 
        partiture: list with the information of the duration of the song and each note.
        fs:Is the sample rate (frequency) given by the person running the program
        note: it is the position of the note in the partiture list. this value changes
        for each module that is done for every note.
    
    The function is elaboraated through the parameters of attack, constant and decay of the instrument
    
    This function returns the variable mod, that provides us an array with the attack, sustain, decay.
    """
    A = get_func(module_list[0], module_list[0][1], fs)
    D = get_func(module_list[2], module_list[2][1], fs)
    if partiture[note][2]-module_list[0][1]>0:
        S = get_func(module_list[1], partiture[note][2]-((len(A)-1)/fs), fs)
    else:
        S = get_func(module_list[1], 1/fs, fs)
    mod = np.concatenate((A, S, S[-1]*D))
    return mod




