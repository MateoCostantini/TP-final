# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:12:18 2022

@author: 54911
"""
import funciones
import numpy as np
import matplotlib.pyplot as plt
import main


def get_instrument():
    harmonics_list = []
    module_list = []
    with open("flute.txt", "r") as f:
        line = f.readline()
        line = int(line)
        for i in range(line):
            line = f.readline()
            harmonic = line.split(" ")
            harmonic[0], harmonic[1] = int(harmonic[0]), float(harmonic[1])
            harmonics_list.append(harmonic)
        for i in range(3):
            line = f.readline()
            module = (line.rstrip()).split(" ")
            for k in range(1, len(module)):
                module[k] = float(module[k])
            module_list.append(module)
    return harmonics_list, module_list


def get_func(param, duration, fs):
    ts = 1/fs
    t = np.arange(0, duration , ts)

    if param[0] == "CONSTANT":
        array = funciones.CONSTANT(t)
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


def get_module(module_list):
    A = get_func(module_list[0], module_list[0][1], 44100)
    S = get_func(module_list[1], 0.5, 44100)
    D = get_func(module_list[2], module_list[2][1], 44100)
    return A, S, D


def join_module():
    attack, sostein, decay = get_module(module_list)
    AS = np.concatenate((attack, sostein))
    module = np.concatenate((AS, decay))
    plt.stem(module)
    return module


