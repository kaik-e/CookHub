from biblioteca.interface import*

while True:
    menu()
    opc_fun = int(input(f"> "))
    # [1] - HUB De Receitas
    if opc_fun == 1:
        menu_Crud()
        opc_crud = int(input(f"> "))

        #[1] - Adicionar Receita
        if opc_crud == 1:
            adicionar_Receita()

        # [2] - Visualizar Receitas
        if opc_crud == 2:
            clear()
            ver_Receitas()
            opc_crud = int(input(f"> "))
            if opc_crud == 1:
                menu_Crud()
            if opc_crud == 2:
                pencerrado()
                break

        # [3] - Atualizar Receitas
        if opc_crud == 3:
            atualizar_Receita()

        # [4] - Excluir Receitas
        if opc_crud == 4:
            deletar_Receita()

        # [5] - Voltar
        if opc_crud == 5:
            menu()

        # [6] - Sair
        if opc_crud == 6:
            pencerrado()
            break

    # [2] - Filtragem Por País
    if opc_fun == 2:
        filtrar_Pais()

    # [3] - Lista de Favoritos
    if opc_fun == 3:
        menu_Favoritos()
        opc_fav = int(input(f"> "))

        # Adicionar Receitas aos Favoritos
        if opc_fav == 1:
            marcar_Favorito()

        # Exibir Receitas Favoritadas
        if opc_fav == 2:
            clear()
            ver_Favoritos()
            opc_fav = int(input(f"> "))
            if opc_fav == 1:
                menu()
            if opc_fav == 2:
                pencerrado()
                break

        # Voltar
        if opc_fav == 3:
            menu_Crud()

        # Sair
        if opc_fav == 4:
            pencerrado()
            break

    # [4] - Sugestão de Recieta Aleatória
    if opc_fun == 4:
        receita_Aleatoria()

    # [5] - Contador de Receitas
    if opc_fun == 5:
        contar_Receitas()

    # [6] - Sair
    if opc_fun == 6:
        pencerrado()
        break