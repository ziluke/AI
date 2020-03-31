# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:09:49 2020

@author: Lucas
"""

import Lab_1_C_Sudoku as sudo
import Lab_1_C_Cryptarithmetic as crypto
import Lab_1_C_Geometric as geo

def menu():
    opt = int(input("1. Sudoku\n2. Crypto\n3. Geometric\nOption: "))
    option = {1: sudo, 2: crypto, 3: geo}
    option[opt].menu()

if __name__ == "__main__":
    menu()