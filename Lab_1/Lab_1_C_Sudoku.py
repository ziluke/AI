# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:26:21 2020

@author: Lucas
"""
import copy
import numpy as np
from math import sqrt

def read_board(option):
    opt = {1: "board_4x4.txt", 2:"board_9x9.txt"}
    f = open(opt[option], "r")
    size = int(f.readline().strip('\n'))
    board = np.zeros((size,size), dtype=int)
    for i in range(size):
        row = f.readline().strip('\n').split(' ')
        for j in range(size):
            board[i][j] = int(row[j])
    f.close()
    return size, board

def check_board(size, board):
    for i in range(size):
        for j in range(size):
            if board[i][j]==0:
                return False

    for i in range(size):
        aux = []
        for j in range(size):
            if board[i][j] in aux:
                return False
            aux.append(board[i][j])

    for i in range(size):
        aux = []
        for j in  range(size):
            if board[j][i] in aux:
                return False
            aux.append(board[j][i])
            
    root = int(sqrt(size))
    for a in range(root):
        for b in range(root):
            aux=[]
            for i in range(root):
                for j in range(root):
                    if board[a*root + i][ b*root + j] in aux:
                        return False
                    aux.append(board[a*root + i][ b*root + j])

    return True            

def generate_solution(size, board):
    np.random.seed()
    aux = copy.deepcopy(board)
    for i in range(size):
        for j in range(size):
            if aux[i][j] == 0:
                aux[i][j] = np.random.randint(1,high=size+1,size=1)
    return aux

def find_solution(size, board, tries):
    while tries > 0:
        aux = generate_solution(size, board)
        if check_board(size, aux):
            return aux
        #print(aux)
        print("tries ", tries)
        tries-=1
    return False

def menu():
    option = int(input("1. Board 4x4\n 2.Board 9x9\nOption: "))
    size, board = read_board(option) 
    tries = int(input("\nInput number of tries: "))
    sol = find_solution(size, board, tries)
    if sol is False:
        print("No solution was found in ",tries, " tries!")
    else:
        print("We found a solution for board of size ",size,": \n",sol)
        f = open("solutions.txt","a")
        f.write("\nSolution for Sudoku:\n")
        #np.savetxt("solutions1.txt", sol)
        f.write(str(sol))
        f.close()

if __name__ == '__main__':
    menu()
    
  