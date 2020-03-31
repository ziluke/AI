from ui import UI
from ctrl import Controller
from state import State
from prb import Problem

    
if __name__ == '__main__':
    f = open("board.txt", "r")
    size = int(f.readline())
    state = State(size)
    prb = Problem(state)
    ctrl = Controller(prb)
    main = UI(ctrl)
    main.runConsole()
    
    
    
    
    
    
    
    
    
    
    
    
    
    