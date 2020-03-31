# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:38:46 2020

@author: Lucas
"""

class Problem:
    def __init__(self, initState):
        self.__initS = initState
    
    def getInitState(self):
        return self.__initS
    
    def solved(self, S):
        return S.solution()
    
    def expand(self, currS):
        return currS.nextConfig()
    
    def heuristic(self, S):
        if not S.isValid():
            return -1
        return S.getBoard().sum()
    


