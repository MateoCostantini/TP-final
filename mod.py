# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:12:18 2022

@author: 54911
"""
import functions
import numpy as np


def get_func(param, duration, fs):
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


def get_mod(module_list, partiture, fs):
    A = get_func(module_list[0], module_list[0][1], fs)
    S = get_func(module_list[1], partiture[0][2]-module_list[0][1], fs)
    D = get_func(module_list[2], module_list[2][1], fs)
    mod = np.concatenate((A, S, D))
    
    return mod




