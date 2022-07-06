# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:47:16 2022

@author: Nusa
"""

from functions import CONSTANT
from functions import LINEAR
from functions import INVLINEAR
from functions import SIN
from functions import EXP
from functions import INVEXP
from functions import QUARTCOS
from functions import QUARTSIN
from functions import HALFCOS
from functions import HALFSIN
from functions import LOG
from functions import INVLOG
from functions import TRI
from functions import PULSES



def test_CONSTANT():
    t = 9
    assert CONSTANT(t) == 9, 'Not passed'


def test_LINEAR():
    t = 9
    t0 = 3
    assert LINEAR(t, t0) == 3, 'Not passed'


def test_INVLINEAR():
    t = 9
    t0 = 3
    assert INVLINEAR(t, t0) == -2, 'Not passed'
    

def test_SIN():
    t = 9
    a = 1
    f = 2
    assert SIN(t, a, f) == 0.24901275322832384 , 'Not passed'


def test_EXP():
    t = 9
    t0 = 3
    assert EXP(t, t0) == 22026.46579 ,  'Not passed'


def test_INVEXP():
    t = 9
    t0 = 3
    assert INVEXP(t, t0) == 3.059023205/100000000, 'Not passed'



def test_QUARTCOS():
    t = 9
    t0 = 3
    assert QUARTCOS(t, t0)== 0, 'Not passed'
    

def test_QUARTSIN():
    t = 9
    t0 = 3
    assert QUARTSIN(t, t0)== -1, 'Not passed'


def test_HALFCOS():
    t = 9
    t0 = 3
    assert HALFCOS(t, t0) == 1, 'Not passed'


def test_HALFSIN():
    t = 9
    t0 = 3
    assert HALFSIN(t, t0) == 1/2, 'Not passed'


def test_LOG():
    t = 9
    t0 = 3
    assert LOG(t, t0) == 1.447158031, 'Not passed'
    
    
def test_INVLOG():
    t = -1 #(array1)
    t = 9 #(array2)
    t0 = 3
    ts = 2
    assert INVLOG(t, t0, ts) == (1.243038049 , 0), 'Not passed'


def test_TRI():
    t = 0 #(array1)
    t = 9 #(array2)
    t0 = 3
    t1 = 1
    a1 = 4
    ts = 2
    assert TRI(t, t0, t1, a1, ts) == (0 , -11/4), 'Not passed'


def test_PULSES():
    t = 9
    t0 = 3
    t1 = 1
    a1 = 4
    assert PULSES(t, t0, t1, a1) == (10, 1), 'Not passed'