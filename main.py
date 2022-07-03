# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:46:50 2022

@author: 54911
"""
import analyze_files
import module
import harmonics
import matplotlib.pyplot as plt


fs = 44100
def main(fs):
    harmonics_list, module_list = analyze_files.get_instrument()
    partiture = analyze_files.get_partiture()
    mod = module.get_mod(module_list, partiture, fs)
    notes = harmonics.get_tone(harmonics_list, partiture, fs)
    return mod, notes


if __name__ == "__main__":
    print(main(fs))