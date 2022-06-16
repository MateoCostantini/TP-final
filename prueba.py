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
param2 = ["INVLINEAR", 0.07]

duration = 0.07
fs = 44100


def get_func(param, duration, fs):
    ts = 1/fs
    t = np.arange(0, 0.07, ts)
    if param[0] == "CONSTANT":
        array = funciones.CONSTANT()
    elif param[0] == "LINEAR":
        array = funciones.LINEAR(param[1])
    elif param[0] == "EXP":
        array = funciones.EXP(t, param[1])
    elif param[0] == "TRI":
        array = funciones.TRI(t, param[1], param[2], param[3], ts)
    elif param[0] == "INVLINEAR":
        array1 = funciones.INVLINEAR(t, param[0])
    return array

print(get_func(param, duration, fs))
plt.plot(get_func(param, duration, fs))


