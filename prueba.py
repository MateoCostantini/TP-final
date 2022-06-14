# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:12:18 2022

@author: 54911
"""
import funciones
import numpy as np
import matplotlib.pyplot as plt
import piano

param = funciones.TRI(0.07, 0.02, 1.3)
duration = 0.07
fs = 44100


def get_func(param, duration, fs):
    ts = 1/fs
    t = param[0](np.arange(0, 0.07, ts))
    return plt.plot(t)

get_func(param, duration, fs)