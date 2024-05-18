from biblioteca.interface import*

while True:
    menu_Funcionalides()
    opc_fun = int(input('Selecione uma opção: '))
    # [1] - HUB De Receitas
    if opc_fun == 1:
        menu_Crud()
        opc_crud = int(input('Selecione uma opção: '))
        #[1] - Adicionar Receita
        if opc_crud == 1:
            adicionar_Receita()
        # [2] - Visualizar Receitas
        if opc_crud == 2:
            ver_Receitas()
        # [3] - Atualizar Receitas
        if opc_crud == 3:
            atualizar_Receita()
        # [4] - Excluir Receitas
        if opc_crud == 4:
            deletar_Receita()
        # [5] - Voltar
        if opc_crud == 5:
            menu_Funcionalides()
        # [6] - Sair
        if opc_crud == 6:
            print('Programa Encerrado!')
            break