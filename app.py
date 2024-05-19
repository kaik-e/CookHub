from biblioteca.interface import*

while True:
    try:
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
            clear()
            filtrar_Pais()
            opc_fp = int(input(f"> "))
            if opc_fp == 1:
                menu()
            if opc_fp == 2:
                pencerrado()
                break
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
            clear()
            receita_Aleatoria()
            opc_ra = int(input(f"> "))
            if opc_ra == 1:
                menu()
            if opc_ra == 2:
                pencerrado()
                break

        # [5] - Contador de Receitas
        if opc_fun == 5:
            clear()
            contar_Receitas()
            opc_cr = int(input(f"> "))
            if opc_cr == 1:
                menu()
            if opc_cr == 2:
                pencerrado()
                break
        # [6] - Sair
        if opc_fun == 6:
            pencerrado()
            break
    except ValueError:
        print("Erro")
        