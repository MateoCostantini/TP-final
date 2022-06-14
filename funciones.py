# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:42:21 2022

@author: 54911
"""

import numpy as np
import matplotlib.pyplot as plt

def CONSTANT(t):
    return 1


def LINEAR(t, t0):
    return t/t0


def INVLINEAR(t, t0):
    return max([1-t/t0, 0])


def SIN(t, a, f):
    return 1 + a*np.sin(f*t)


def EXP(t, t0):
    return np.e**(5*(t-t0))/t0


def INVEXP(t, t0):
    return np.e**(-5*t)/t0


def QUARTCOS(t, t0):
    return np.cos((np.pi*t)/(2*t))


def QUARTSIN(t, t0):
    return np.sin((np.pi*t)/(2*t0))


def HALFCOS(t, t0):
    return (1+np.cos((np.pi*t)/t0))/2


def HALFSIN(t, t0):
    return (1+np.cos(np.pi((t/t0)-0.5)))/2


def LOG(t, t0):
    return np.log10(((9*t)/t0)+1)


def INVLOG(t, t0):
    if t<t0:
        return np.log10(((-9*t)/t0)+10)
    else:
        return 0


def TRI(t0, t1, a1):
    if t<t1:
        return (t*a1)/t1
    elif t>t1:
        return (t-t1)/(t1-t0) + a1
    
    
def PULSES(t, t0, t1, a1):
    pass
    
    
    
    
    