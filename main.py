# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:46:50 2022

@author: 54911
"""
import instrument

def main():
    harmonics_list, module_list = instrument.get_instrument()
    module = instrument.join_module(module_list)
    return module


if __name__ == "__main__":
    print(main())