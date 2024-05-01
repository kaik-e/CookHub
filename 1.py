import os
clear = lambda: os.system('cls')
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

print(bcolors.WARNING + 
f"""
{bcolors.CVIOLET}+----------------------------+
{bcolors.CVIOLET}|{bcolors.CWHITE}░█▀▀░█▀█░█▀█░█░█░█░█░█░█░█▀▄{bcolors.CVIOLET}|
{bcolors.CVIOLET}|{bcolors.CWHITE}░█░░░█░█░█░█░█▀▄░█▀█░█░█░█▀▄{bcolors.CVIOLET}|
{bcolors.CVIOLET}|{bcolors.CWHITE}░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░{bcolors.CVIOLET}|
{bcolors.CVIOLET}+----------------------------+
""" + bcolors.ENDC)

print(f""" {bcolors.CVIOLET}≈  {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Receitas
 {bcolors.CBLUE}✶  {bcolors.BOLD}{bcolors.CWHITE}2 {bcolors.ENDC}Favoritos 
 {bcolors.WARNING}⚡︎ {bcolors.BOLD}{bcolors.CWHITE}3 {bcolors.ENDC}Receita aleatoria
 {bcolors.CRED}⤫  {bcolors.BOLD}{bcolors.CWHITE}4 {bcolors.ENDC}Sair
""")

select = int(input(f"> "))

if select == 1:
    clear()
    print(f""" {bcolors.CWHITE}({bcolors.CVIOLET}≈{bcolors.CWHITE})
  {bcolors.WARNING}⤷ {bcolors.CBLUE}✎ {bcolors.BOLD}{bcolors.CWHITE}1 {bcolors.ENDC}Cadastrar receita          
    {bcolors.CVIOLET}✐ {bcolors.BOLD}{bcolors.CWHITE}2 {bcolors.ENDC}CRUD
    {bcolors.CRED}↺ {bcolors.BOLD}{bcolors.CWHITE}3 {bcolors.ENDC}Voltar
""")
    select = int(input(f"> "))
if select == 2:
    print("Fodase 2")    