#Biblioteca de utilidades pessoal!#
from os import system as sys

r"""Biblioteca de utilidades.

Este arquivo sera usada para encurtar e manipular seu código de forma simples.

"""

def cls():
    '''Limpar terminal'''
    sys('cls')

def linha():
    return print('\033[1;32m=\033[m'*40)
    
def cabeçalho(texto):
    '''
    Formatação para cabeçalho centralizado.
    '''
    linha()
    print(f'\n\033[1;32m{texto:^40}\033[m\n')
    linha()
    print()

def lista(texto):
    '''
    Criar lista em forma numérica.
\n  Separe a entrada com virgula.
\n  Exemplo: lista(texto,texto)
    '''
    lista = texto.split(",") #Separar input de palavras
    numero_palavras = len(lista) #Contar as palavras
    numero_lista = 1 #
    
    for i in range(0,numero_palavras):
        print(f'''\t \033[1;36m{numero_lista}.{lista[i]}\033[m''')
        numero_lista += 1
    print()

