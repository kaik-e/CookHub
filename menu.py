## (OPT = OPÇAO) <- opt pega o numero dentro dos submenus para continuar a logica dos menus 

## vai se foder
import os
clear = lambda: os.system('cls')

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
    clear()
    print(c.WARNING + 
    f"""
    {c.VIOLETA}+----------------------------+
    {c.VIOLETA}|{c.BRANCO}░█▀▀░█▀█░█▀█░█░█░█░█░█░█░█▀▄{c.VIOLETA}|
    {c.VIOLETA}|{c.BRANCO}░█░░░█░█░█░█░█▀▄░█▀█░█░█░█▀▄{c.VIOLETA}|
    {c.VIOLETA}|{c.BRANCO}░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░{c.VIOLETA}|
    {c.VIOLETA}+----------------------------+
    """ + c.END)

    print(f"""    {c.VIOLETA}≈  {c.BOLD}{c.BRANCO}1 {c.END}Receitas
    {c.AZUL}✶  {c.BOLD}{c.BRANCO}2 {c.END}Favoritos 
    {c.WARNING}?  {c.BOLD}{c.BRANCO}3 {c.END}Receita aleatoria
    {c.VERMELHO}⤫  {c.BOLD}{c.BRANCO}4 {c.END}Sair
    """)

## Função receitas
def receitas():
        clear()
        print(f""" {c.BRANCO}({c.VIOLETA}≈{c.BRANCO})
              
    {c.AZUL}✎  {c.BOLD}{c.BRANCO}1 {c.END}Cadastrar receita          
    {c.VIOLETA}✐  {c.BOLD}{c.BRANCO}2 {c.END}CRUD
    {c.VERMELHO}↺  {c.BOLD}{c.BRANCO}3 {c.END}Voltar
    """)
        #parte logica da função
        opt = int(input(f"> "))
        if opt == 1:
            cr()
        if opt == 2:
            crud()
        if opt == 3:

            pass

## Função favoritos
def favoritos():
    clear()
    print(f""" {c.BRANCO}({c.AZUL}✶{c.BRANCO})
    
    Under construction 🔧
    {c.VERMELHO}↺  {c.BOLD}{c.BRANCO}1 {c.END}Voltar
    """)
    
    #parte logica da função
    opt = int(input(f"> "))
    if opt == 1:
        pass

## Função receita aleatoria
def ra():
    clear()
    print(f""" {c.BRANCO}({c.WARNING}?{c.BRANCO})
    
    Under construction 🔧
    {c.VERMELHO}↺  {c.BOLD}{c.BRANCO}1 {c.END}Voltar
    """)
    
    #parte logica da função
    opt = int(input(f"> "))
    if opt == 1:
        pass
                

## Função criar receitas
def cr():
    clear()
    print(f"""  Under construction 🔧
    {c.VERMELHO}↺  {c.BOLD}{c.BRANCO}1 {c.END}Voltar""")
    
    opt = int(input(f"> "))
    if opt == 1:
        receitas()
## Função crud
def crud():
    clear()
    print(f"""  Under construction 🔧
    {c.VERMELHO}↺  {c.BOLD}{c.BRANCO}1 {c.END}Voltar""")
    
    opt = int(input(f"> "))
    if opt == 1:
        receitas()

