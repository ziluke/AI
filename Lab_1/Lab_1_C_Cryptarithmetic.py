# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:46:58 2020

@author: Lucas
"""
import numpy as np
import copy

def read_words():
    words = []
    symbol = ''
    aux = ''
    
    while aux != '=':
        word = input("Enter word: ")
        words.append(word)
        aux = input("Enter symbol (+,-,=): ")
        if aux != '=':
            symbol = aux
    result = input("Enter result: ")
    
    letters = {}
    for w in words:
        for l in w:
            letters[l]=''
    for l in result:
        letters[l]=''
    return letters, symbol, words, result
    
def generate_solution(letters):
    aux = copy.deepcopy(letters)
    for l in aux:
        aux[l] = hex(np.random.randint(0,high=16))
    return aux

def transform_Hex_Dec(letters, words, result):
    word_val = []
    for word in words:
        aux = ''
        for l in word:
            aux += letters[l][2]
        aux = int(aux, 16)
        word_val.append(aux)
    
    res_val = ''

    for l in result:
        res_val += letters[l][2]
    res_val = int(res_val, 16)
    
    return word_val, res_val

def test_solution(letters, symbol, words, result):
    for w in words:
        if letters[w[0]] == '0x0':
            return False

    if letters[result[0]] == '0x0':
        return False
        
    word_val, res_val = transform_Hex_Dec(letters, words, result)
    if symbol =="+":
        if sum(word_val) == res_val:
            return True
    else:
        if word_val[0]-sum(word_val[1:]) == res_val:
            return True
    return False
    
def find_solution(letters, symbol, words, result, tries):
    while tries > 0:
        aux = generate_solution(letters)
        print(aux,'\n',tries)
        ok = test_solution(aux, symbol, words, result)
        if ok is True:
            return aux
        tries-=1
    return False

def menu():
    letters, symbol, words, result = read_words()
    tries = int(input("Enter number of tries: "))
    sol = find_solution(letters, symbol, words, result, tries)
    if sol is False:
        print("A solution has not been found in ",tries," tries!")
    else:
        print(letters,"\n",words,"\n",result,"\n",sol)
        f = open("solutions.txt","a")
        f.write("\nSolution for Crypt:\n")
        f.write(str(sol))
        f.close()
    

if __name__ == '__main__':
    menu()