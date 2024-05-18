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
    # [2] - Filtragem Por País
    if opc_fun == 2:
        filtrar_Pais()
    # [3] - Lista de Favoritos
    if opc_fun == 3:
        menu_Favoritos()
        opc_fav = int(input('Selecione uma opção: '))
        # Adicionar Receitas aos Favoritos
        if opc_fav == 1:
            marcar_Favorito()
        # Exibir Receitas Favoritadas
        if opc_fav == 2:
            ver_Favoritos()
        # Voltar
        if opc_fav == 3:
            menu_Crud()
        # Sair
        if opc_fav == 4:
            print('Programa Encerrado!')
            break
    # [4] - Sugestão de Recieta Aleatória
    if opc_fun == 4:
        receita_Aleatoria()
    # [5] - Contador de Receitas
    if opc_fun == 5:
        contar_Receitas()
    # [6] - Sair
    if opc_fun == 6:
        print('Programa Encerrado!')
        break