from biblioteca.interface import*

while True:
    menu_Funcionalides()
    opc_fun = int(input('Selecione uma opção: '))
    # [1] - HUB De Receitas
    if opc_fun == 1:
        menu_Crud()
        opc_crud = int(input('Selecione uma opção: '))
