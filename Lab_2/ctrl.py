# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:37:21 2020

@author: Lucas
"""

class Controller:
    def __init__(self, p):
        self.__problem = p
    
    def order(self, queue):
        return sorted(queue, key = lambda x: self.__problem.heuristic(x), reverse=True)
    
    def DFS(self):
        stack = [self.__problem.getInitState()]
        while stack:
            currS = stack.pop(0)
            if self.__problem.solved(currS):
                return currS
            aux = self.__problem.expand(currS)
            if aux != []:
                stack += aux
        return None
    
    def greedy(self):
        queue = [self.__problem.getInitState()]    
        while queue:
            currS = queue.pop(0)
            if self.__problem.solved(currS):
                return currS
            aux = self.__problem.expand(currS)
            if aux != []:
                queue += aux
            queue = self.order(queue)
        return None

    