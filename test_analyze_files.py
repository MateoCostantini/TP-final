#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:30:28 2022

@author: tato
"""


from analyze_files import get_instrument
from analyze_files import get_partiture

def test_get_instrument():
    harmonics, module = get_instrument("piano.txt")
    assert harmonics == [(1, 1),(2, 0.72727272), (3, 0.31818181), (4, 0.090909)] , "not passed"
    assert module == [('LINEAR', 0.02), ('CONSTANT',), ('INVEXP', 0.06)] , "not passed"

def test_get_partiture():
    assert get_partiture("partiture.txt") == [(0, 261.626, 0.5), (0.5, 293.665, 0.5), (1, 329.628, 0.5), (1.2, 261.626, 0.7)] , "not passed"