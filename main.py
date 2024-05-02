import os
from menu import *
clear = lambda: os.system('cls')

while True:
    clear()
    menu()
    select = int(input(f"> "))
    
    if select == 1:
        clear()
        receitas()
    
        opt = int(input(f"> "))
        
        if opt == 1:
            clear()
            cr()
        if opt == 2:
            clear()
            crud()
        if opt == 3:
            clear()
            pass
        