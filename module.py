# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:25:54 2022

@author: Nusa
"""

import functions
import harmonics
import numpy as np


def get_func(param, duration, fs): #1
    """
    This function allowes the user to choose between the module functions, CONSTANT, LINEAR, TRI
    and INVLINEAR.
    
    In this functions enters:
        param: A list that contains the type of function ans it's parameters
        duration: The duration of the function
        fs: Is the sample rate that is measured in Hz, given by the person running the program
        
    This function returns the function elected.
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


def get_mod(module_list, partiture, fs, sound): #2
    """
    This function recives module_list, partiture, fs and the sound
        module_list: Is a list with all the modules of the function get_instrument. 
        partiture: Partiture provides us with the information od the duration of the song and each note.
        fs:Is the frequency given by the person running the program
        sound: Is the function elaborated in the main archive, that produces sounds with the arguments given.
    
    The function is elaboraated through the parameters of attack, constant and decay of the instrument
    
    This function returns the variable mod, that provides us with grafical information of the sound.
    
    """
    A = get_func(module_list[0], module_list[0][1], fs)
    D = get_func(module_list[2], module_list[2][1], fs)
    if partiture[sound][2]-module_list[0][1]>0:
        S = get_func(module_list[1], partiture[sound][2]-((len(A)-1)/fs), fs)
    else:
        S = get_func(module_list[1], 1/fs, fs)
    mod = np.concatenate((A, S, S[-1]*D))
    return mod