# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:34:59 2020

@author: Lucas
"""

    
class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
    
    def runDFS(self):
        return self.__ctrl.DFS()
    
    def runGreedy(self):
        return self.__ctrl.greedy()
        
    def runConsole(self):
        print("1.Resolve using DFS\n2.Resolve using Greedy\n")
        opt = int(input("Option: "))
        options = {1:self.runDFS, 2:self.runGreedy}
        res = options[opt]()
        if res is None:
            print("No solution could be found!\n")
        else:
            print(res.getBoard())
    