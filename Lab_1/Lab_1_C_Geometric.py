# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:09:00 2020

@author: Lucas
"""
import numpy as np
import copy

def insertGeo1(mat, row, col):
    mat[row][col]*=2
    mat[row][col+1]*=2
    mat[row][col+2]*=2
    mat[row-1][col]*=2
    return mat

def insertGeo2(mat, row, col):
    mat[row][col]*=3
    mat[row][col+1]*=3
    mat[row][col+2]*=3
    mat[row+1][col+2]*=3
    return mat

def insertGeo3(mat, row, col):
    mat[row][col]*=4
    mat[row][col+1]*=4
    mat[row][col+2]*=4
    mat[row-1][col+1]*=4
    return mat

def insertGeo4(mat, row, col):
    mat[row][col]*=5
    mat[row][col+1]*=5
    mat[row][col+2]*=5
    mat[row-1][col]*=5
    mat[row-1][col+2]*=5
    return mat

def insertGeo5(mat, row, col):
    mat[row][col]*=7
    mat[row][col+1]*=7
    mat[row][col+2]*=7
    mat[row][col+3]*=7
    return mat

def gen_row_col():
    row = np.random.randint(0,5)
    col = np.random.randint(0,6)
    return row,col

def generate_solution(mat):
    aux = copy.deepcopy(mat)
    row,col = gen_row_col()
    aux = insertGeo1(aux, row, col)
    row,col = gen_row_col()
    aux = insertGeo2(aux, row, col)
    row,col = gen_row_col()
    aux = insertGeo3(aux, row, col)
    row,col = gen_row_col()
    aux = insertGeo4(aux, row, col)
    row,col = gen_row_col()
    aux = insertGeo5(aux, row, col)
    return aux
    
def test_solution(mat):
    #print(mat)
    for i in range(5):
        for j in range(6):
            if mat[i][j] not in [1,2,3,4,5,7]:
                return False
    return True

def find_solution(mat, tries):
    while tries > 0:
        try:
            aux = generate_solution(mat)
            if test_solution(aux):
                return aux
        except IndexError:
            pass
        tries-=1
    return False

def menu():
    mat = [[1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1],
           [1,1,1,1,1,1]]
    tries = int(input("Enter number of tries: "))
    sol = find_solution(mat, tries)
    if sol is False:
        print("The solution couldn't be found in ",tries," tries!\n")
    else:
        print("Solution:\n",np.asmatrix(sol))
        f = open("solutions.txt","a")
        f.write('\nSolution for Geometric:\n'),
        string = ''
        for i in sol:
            for j in i:
                string = string+str(j)+" "
            string +='\n'
        f.write(string)
        f.close()

if __name__ == '__main__':
    menu()
    
    
    
    
    
    
    
    