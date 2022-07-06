#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 00:21:29 2022

@author: tato
"""
import numpy as np
from module import get_func
from module import get_mod

def test_get_func():
    param = ["CONSTANT"]
    duration = 4
    fs = 0.5
    assert get_func(param, duration, fs) == [1., 1., 1., 1., 1., 1., 1., 1.] , "not passed"
    
def test_get_mod():
    module_list = [['LINEAR', 0.02], ['CONSTANT'], ['INVEXP', 0.06]]
    partiture = [(0, "C4", 0.5)]
    fs = 100
    assert get_mod(module_list, partiture, fs) == np.array([0., 0.5], [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.], [1., 0.43459821, 0.1888756 , 0.082085  , 0.03567399, 0.01550385]) ,"not passed"
    