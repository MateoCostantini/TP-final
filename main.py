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
def notes(fs):
    ts = 1/fs
    harmonics_list, module_list = analyze_files.get_instrument()
    partiture = analyze_files.get_partiture()
    mods = module.get_mod(module_list, partiture, fs)
    notes = harmonics.get_tone(harmonics_list, partiture, fs)
    track = harmonics.final_partiture(notes, mods, partiture, ts)
    return track

def main():
    print(notes(fs))


if __name__ == "__main__":
    main()