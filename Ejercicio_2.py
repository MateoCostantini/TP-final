# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:47:27 2022

@author: 54911
"""

import math



def get_instrument():
    instrument_list = []
    with open("flute.txt", "r") as f:
        line = f.readline()
        line = int(line)
        instrument_list.append(line)
        for i in range(line):
            line = f.readline()
            armonic = line.split(" ")
            armonic[0], armonic[1] = int(armonic[0]), float(armonic[1])
            instrument_list.append(armonic)
        for i in range(3):
            line = f.readline()
            module = line.split(" ")
            for k in range(1, len(module)):
                module[k] = float(module[k])
            instrument_list.append(module)
    return instrument_list

def gen_mod(instrumento, d, fs):
    return

constant = 1
linear = lambda x,t: x/t
invlinear = lambda x,t: max(1-(x/t), 0)
sin = lambda x,a,f: 1 + a*math.sin(f*x)
Exp = lambda x,t: math.e ** (5*(x-t))/t
invexp = lambda x,t: math.e ** (-5*x)/t
quartcos = lambda x,t: math.cos((math.pi * x)/(2 * t))
quartsin = lambda x,t: math.sin((math.pi * x)/(2 * t))
halfcos = lambda x,t: (1 + math.cos((math.pi * x)/ t))/2
halfsin = lambda x,t: (1 + math.cos(math.pi * ((x/t)-(1/2))))/2
Log = lambda x,t: math.log(((9 * x)/ t)+1, 10)