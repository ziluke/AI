# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:37:55 2020

@author: Lucas
"""

import numpy
import copy

class State:
    def __init__(self, size):
        self.__size = size
        self.__board = numpy.zeros((size, size), dtype=int)
    
    def setBoard(self, board):
        self.__board = board
    
    def getBoard(self):
        return self.__board
    
    def solution(self):
        return self.__board.sum() == self.__size and self.isValid()
    
    def validPos(self, i, j):
        for r in range(self.__size): 
            for c in range(self.__size):
                if i != r or j != c:
                    if self.__board[r][c] == 1:
                        if i == r or j == c:
                            return False
                        if abs(i - r) == abs(j - c):
                            return False
        return True
    
    def nextConfig(self):
        configs = []
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__board[i][j] != 1 and self.validPos(i, j):
                    cpy = copy.deepcopy(self.__board)
                    cpy[i][j] = 1
                    state = State(self.__size)
                    state.setBoard(cpy)
                    configs.append(state)
        return configs
                    
            
    def isValid(self):
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__board[i][j] == 1 and not self.validPos(i, j):
                    return False
        return True
    