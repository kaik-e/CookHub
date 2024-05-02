import os
from menu import *
clear = lambda: os.system('cls')

while True:
    menu()
    select = int(input(f"> "))

    if select == 1:
        receitas()
    if select == 2:
        favoritos()
    if select == 3:
        ra()
    if select == 4:
        break
    
  