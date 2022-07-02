# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:46:50 2022

@author: 54911
"""
import analyze_files
import instrument


def main():
    harmonics_list, module_list = analyze_files.get_instrument()
    partiture = analyze_files.get_partiture()
    module = instrument.get_module(module_list)
    return module


if __name__ == "__main__":
    print(main())