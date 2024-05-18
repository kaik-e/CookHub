import os
clear = lambda: os.system('cls')
import random
## Classe de cores, (c.) <- prefixo -> Ex: (c.COR)
class c:
    WARNING = '\033[93m'    #Codigo de cor para avisos
    FAIL = '\033[91m'   #Codigo de cor para erros
    END = '\033[0m'     #Termina a cor no texto
    BOLD = '\033[1m'    #Deixa o texto em negrito
    BLINK = '\033[5m'   #Faz o texto piscar 
    UNDERLINE = '\033[4m'   #Coloca uma linha embaixo do texto
    PRETO  = '\33[30m'
    VERMELHO    = '\33[31m'
    VERDE  = '\33[32m'
    AMARELO = '\33[33m'
    AZUL   = '\33[34m'
    VIOLETA = '\33[35m'
    BEGE  = '\33[36m'
    BRANCO  = '\33[37m'

## Função menu
def menu():
    print(c.WARNING + 
    f"""
    {c.VIOLETA}+----------------------------+
    {c.VIOLETA}|{c.BRANCO}░█▀▀░█▀█░█▀█░█░█░█░█░█░█░█▀▄{c.VIOLETA}|
    {c.VIOLETA}|{c.BRANCO}░█░░░█░█░█░█░█▀▄░█▀█░█░█░█▀▄{c.VIOLETA}|
    {c.VIOLETA}|{c.BRANCO}░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░{c.VIOLETA}|
    {c.VIOLETA}+----------------------------+
    """ + c.END)

    print(f"""    {c.VIOLETA}≈  {c.BOLD}{c.BRANCO}1 {c.END}Hub de Receitas
    {c.AZUL}◍  {c.BOLD}{c.BRANCO}2 {c.END}Filtragem por país      
    {c.AZUL}✶  {c.BOLD}{c.BRANCO}3 {c.END}Favoritos 
    {c.WARNING}?  {c.BOLD}{c.BRANCO}4 {c.END}Receita aleatoria
    {c.WARNING}∘  {c.BOLD}{c.BRANCO}5 {c.END}Contador de receiras
    {c.VERMELHO}⤫  {c.BOLD}{c.BRANCO}6 {c.END}Sair
    """) 

def menu_Crud():
        clear()
        print(f""" {c.BRANCO}({c.VIOLETA}≈{c.BRANCO})
              
    {c.AZUL}✎  {c.BOLD}{c.BRANCO}1 {c.END}Cadastrar receita
    {c.AZUL}✺  {c.BOLD}{c.BRANCO}2 {c.END}Visualizar receitas           
    {c.VIOLETA}✐  {c.BOLD}{c.BRANCO}3 {c.END}Atualizar receitas
    {c.VIOLETA}⚠  {c.BOLD}{c.BRANCO}4 {c.END}Excluir receitas
    {c.VERMELHO}↺  {c.BOLD}{c.BRANCO}5 {c.END}Voltar
    {c.VERMELHO}⤫  {c.BOLD}{c.BRANCO}6 {c.END}Sair
    """)

def menu_Favoritos():
    
    print('COOKHUB v1.0')
    
    print('[1] - Adicionar Receita aos Favoritos')
    print('[2] - Mostrar as Receitas Favoritadas')
    print('[3] - Voltar')
    print('[4] - Sair')
    

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
    print(f"\n{c.VIOLETA}✺  {c.BRANCO}Lista de Receitas:"'\n')
    print(file.read())
    print(f"""
    {c.VERMELHO}↺  {c.BOLD}{c.BRANCO}1 {c.END}Voltar
    {c.VERMELHO}⤫  {c.BOLD}{c.BRANCO}2 {c.END}Sair
    """)

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
def marcar_Favorito():
    nome = input("Digite o nome da receita que deseja marcar como favorita: ").title()
    if not os.path.exists("receitas.txt"):
        print("Não existem receitas para marcar como favorita.")
        return
    
    file = open("receitas.txt","r", encoding='utf-8')
    linhas = file.readlines()

    encontrada = False
    file = open("receitas.txt","w", encoding='utf-8')
    for i in range(0, len(linhas), 5):
        if linhas[i].strip() == f"Nome: {nome}":
            file.write(f"Nome: {nome} (Favorita)\n")
            for j in range(1, 4):
                file.write(linhas[i + j])
            encontrada = True
        else:
            file.write("".join(linhas[i:i+5]))

    if encontrada:
        print("Receita marcada como favorita!")
    else:
        print("Receita não encontrada.")

# Função para visualizar as receitas favoritas
def ver_Favoritos():
    file = open("receitas.txt","r", encoding='utf-8')
    print("\nLista de Receitas Favoritas:")
    for linha in file:
        if "(Favorita)" in linha:
            print(linha.strip())
            for _ in range(3):  # Pula as próximas três linhas (país, ingredientes, modo de preparo)
                next(file)
def contar_Receitas():
    count = 0
    file = open("receitas.txt","r", encoding='utf-8')
    for line in file:
        if line.strip() == "":
            count += 1
    print(f"Total de receitas cadastradas: {count}")

def receita_Aleatoria():
    file = open("receitas.txt","r", encoding='utf-8')
    receitas = file.read().split("\n\n")  # Divide o arquivo em blocos separados por duas quebras de linha
    receita_aleatoria = random.choice(receitas)
    print("\nReceita Aleatória:")
    print(receita_aleatoria)

