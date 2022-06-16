# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:12:18 2022

@author: 54911
"""
import funciones
import numpy as np
import matplotlib.pyplot as plt

param = ["TRI", 0.07, 0.02, 1.3]
param1 = ["EXP", 0.07]
param2 = ["INVLINEAR", 0.02]
param3 = ["INVEXP", 0.02]
param4 = ["SIN", 5, 10.3]
param5 = ["INVLOG", 0.5]

duration = 1.07
fs = 44100


def get_func(param, duration, fs):
    ts = 1/fs
    t = np.arange(0, duration , ts)
    if param[0] == "CONSTANT":
        array = funciones.CONSTANT()
    elif param[0] == "LINEAR":
        array = funciones.LINEAR(t, param[1])
    elif param[0] == "INVLINEAR":
        array = funciones.INVLINEAR(t, param[1])
    elif param[0] == "SIN": 
        array = funciones.SIN(t, param[1], param[2])
    elif param[0] == "EXP":
        array = funciones.EXP(t, param[1])
    elif param[0] == "INVEXP":
        array = funciones.INVEXP(t, param[1])
    elif param[0] == "QUARTCOS":
        array = funciones.QUARTCOS(t, param[1])
    elif param[0] == "QUARTSIN":
        array = funciones.QUARTSIN(t, param[1])
    elif param[0] == "HALFCOS":
        array = funciones.HALFCOS(t, param[1])
    elif param[0] == "HALFSIN":
        array = funciones.HALFSIN(t, param[1])
    elif param[0] == "LOG":
        array = funciones.LOG(t, param[1])
    elif param[0] == "INVLOG":
        array = funciones.INVLOG(t, param[1], ts)
    elif param[0] == "TRI":
        array = funciones.TRI(t, param[1], param[2], param[3], ts)

    return array

print(get_func(param5, duration, fs))
plt.plot(get_func(param5, duration, fs))


