## (OPT = OPÇAO) <- opt pega o numero dentro dos submenus para continuar a logica dos menus 

import os
clear = lambda: os.system('cls')

## Classe de cores, (bcolors.) <- prefixo -> Ex: (bcolors.COR)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BLINK = '\033[5m'
    UNDERLINE = '\033[4m'
    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

## Função menu
def menu():
    clear()
    print(bcolors.WARNING + 
    f"""
    {bcolors.CVIOLET}+----------------------------+
    {bcolors.CVIOLET}|{bcolors.CWHITE}░█▀▀░█▀█░█▀█░█░█░█░█░█░█░█▀▄{bcolors.CVIOLET}|
    {bcolors.CVIOLET}|{bcolors.CWHITE}░█░░░█░█░█░█░█▀▄░█▀█░█░█░█▀▄{bcolors.CVIOLET}|
    {bcolors.CVIOLET}|{bcolors.CWHITE}░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░{bcolors.CVIOLET}|
    {bcolors.CVIOLET}+----------------------------+
    """ + bcolors.ENDC)

    print(f"""    {bcolors.CVIOLET}≈  {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Receitas
    {bcolors.CBLUE}✶  {bcolors.BOLD}{bcolors.CWHITE}2 {bcolors.ENDC}Favoritos 
    {bcolors.WARNING}?  {bcolors.BOLD}{bcolors.CWHITE}3 {bcolors.ENDC}Receita aleatoria
    {bcolors.CRED}⤫  {bcolors.BOLD}{bcolors.CWHITE}4 {bcolors.ENDC}Sair
    """)

## Função receitas
def receitas():
        clear()
        print(f""" {bcolors.CWHITE}({bcolors.CVIOLET}≈{bcolors.CWHITE})
              
    {bcolors.CBLUE}✎  {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Cadastrar receita          
    {bcolors.CVIOLET}✐  {bcolors.BOLD}{bcolors.CWHITE}2 {bcolors.ENDC}CRUD
    {bcolors.CRED}↺  {bcolors.BOLD}{bcolors.CWHITE}3 {bcolors.ENDC}Voltar
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
    print(f""" {bcolors.CWHITE}({bcolors.CBLUE}✶{bcolors.CWHITE})
    
    Under construction 🔧
    {bcolors.CRED}↺  {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Voltar
    """)
    
    #parte logica da função
    opt = int(input(f"> "))
    if opt == 1:
        receitas()

## Função receita aleatoria
def ra():
    clear()
    print(f""" {bcolors.CWHITE}({bcolors.WARNING}?{bcolors.CWHITE})
    
    Under construction 🔧
    {bcolors.CRED}↺  {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Voltar
    """)
    
    #parte logica da função
    opt = int(input(f"> "))
    if opt == 1:
        receitas()
                

## Função criar receitas
def cr():
    clear()
    print(f"""  Under construction 🔧
    {bcolors.CRED}↺  {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Voltar""")
    
    opt = int(input(f"> "))
    if opt == 1:
        receitas()
## Função crud
def crud():
    clear()
    print(f"""  Under construction 🔧
    {bcolors.CRED}↺  {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Voltar""")
    
    opt = int(input(f"> "))
    if opt == 1:
        receitas()

