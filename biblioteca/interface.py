import os
clear = lambda: os.system('cls')
import random
# Menu temporario, para implementacao
def mostra_Linha():
    print('-='*42)

def menu_Crud():
    mostra_Linha()
    print('HUB de Receitas')
    mostra_Linha()
    print('[1] - Adicionar Receita')
    print('[2] - Visualizar Receitas')
    print('[3] - Atualizar Receitas')
    print('[4] - Excluir Receitas')
    print('[5] - Voltar')
    print('[6] - Sair')
    mostra_Linha()

def menu_Funcionalides():
    mostra_Linha()
    print('COOKHUB v1.0')
    mostra_Linha()
    print('[1] - HUB De Receita')
    print('[2] - Filtragem Por País')
    print('[3] - Lista de Favoritos')
    print('[4] - Sugestão de Recietas Aleatória')
    print('[5] - Contador de Receitas')
    print('[6] - Sair')
    mostra_Linha()

def menu_Favoritos():
    mostra_Linha()
    print('COOKHUB v1.0')
    mostra_Linha()
    print('[1] - Adicionar Receita aos Favoritos')
    print('[2] - Mostrar as Receitas Favoritadas')
    print('[3] - Voltar')
    print('[4] - Sair')
    mostra_Linha()

def adicionar_Receita():
    nome = input("Digite o nome da receita: ").title()
    pais_origem = input("Digite o país de origem da receita: ").title()
    ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ").title()
    modo_preparo = input("Digite o modo de preparo da receita: ").title()
    
    file = open("receitas.txt","a", encoding='utf-8')
    file.write(f"Nome: {nome}\n")
    file.write(f"País de Origem: {pais_origem}\n")
    file.write(f"Ingredientes: {ingredientes}\n")
    file.write(f"Modo de Preparo: {modo_preparo}\n")
    file.write("\n")  # Adiciona uma linha em branco para separar as receitas

    print("Receita adicionada com sucesso!")

# Função para ver todas as receitas
def ver_Receitas():
    file = open("receitas.txt","r", encoding='utf-8')
    print("\nLista de Receitas:"'\n')
    print(file.read())

# Função para filtrar receitas por país de origem
def filtrar_Pais():
    pais = input("Digite o país de origem para filtrar as receitas: ").title()
    file = open("receitas.txt","r", encoding='utf-8')
    print(f"\nReceitas do país '{pais}':")
    encontrada = False
    for linha in file:
        if linha.strip() == f"País de Origem: {pais}":
            for _ in range(3):
                print(next(file).strip())
            encontrada = True

    if not encontrada:
        print("Nenhuma receita encontrada para este país.")

# Função para atualizar uma receita existente
def atualizar_Receita():
    nome = input("Digite o nome da receita que deseja atualizar: ").title()
    if not os.path.exists("receitas.txt"):
        print("Não existem receitas para atualizar.")
        return
    
    file = open("receitas.txt","r", encoding='utf-8')
    linhas = file.readlines()

    encontrada = False
    file = open("receitas.txt","w", encoding='utf-8')
    for i in range(0, len(linhas), 5):
        if linhas[i].strip() == f"Nome: {nome}":
            pais_origem = input("Digite o novo país de origem da receita: ").title()
            ingredientes = input("Digite os novos ingredientes da receita (separados por vírgula): ").title()
            modo_preparo = input("Digite o novo modo de preparo da receita: ").title()
                
            file.write(f"Nome: {nome}\n")
            file.write(f"País de Origem: {pais_origem}\n")
            file.write(f"Ingredientes: {ingredientes}\n")
            file.write(f"Modo de Preparo: {modo_preparo}\n")
            file.write("\n")
            encontrada = True
        else:
            file.write("".join(linhas[i:i+5]))

    if encontrada:
        print("Receita atualizada com sucesso!")
    else:
        print("Receita não encontrada.")

# Função para deletar uma receita existente
def deletar_Receita():
    nome = input("Digite o nome da receita que deseja deletar: ").title()
    if not os.path.exists("receitas.txt"):
        print("Não existem receitas para deletar.")
        return
    
    file = open("receitas.txt","r", encoding='utf-8')
    linhas = file.readlines()

    encontrada = False
    file = open("receitas.txt","w", encoding='utf-8')
    for i in range(0, len(linhas), 5):
        if linhas[i].strip() == f"Nome: {nome}":
            encontrada = True
        else:
            file.write("".join(linhas[i:i+5]))

    if encontrada:
        print("Receita deletada com sucesso!")
    else:
        print("Receita não encontrada.")


