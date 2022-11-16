#################################################
#                                               #
#       Equipe: João, Italo                     #
#       inicio: 15/11/22                        #
#       termino:                                #
#       projeto: Vocabulo                       #
#                                               #
#################################################

#   Imports     #
from Utilidades import *
import random
from os import system as sys
#   Var glob    #


#   def's       #

#Retorna uma palavra aleatoria do arquivo de palavras
def random_palavra(): 
    with open("lista_palavras.txt","r",encoding="UTF-8") as arquivo:
        palavras = arquivo.read()
        return random.choice(palavras.split())
    

#   MAIN        #

#COLOCAR O PROGRAMA EM LOOPING
while True:
    #LIMPAR TERMINAL
    sys("cls") 
    
    #DEFINIR NUMERO DE RODADAS
    rodadas = 5
    
    #SEPARAR VARIAVEL PARA GUARDAR INPUT DO USUARIO
    palpites = ''
    
    #DEFINIR PALAVRA SORTEADA
    palavra = random_palavra() 

    while rodadas > 0:
        
        #LIMPAR TERMINAL
        sys("cls") 
        
        #GERAR CABEÇALHO CENTRALIZADO
        cabeçalho("VOCABULO") 
        
        #INFORMAR NUMERO DE CHANCES
        print(f"\033[0;33mNumero de chances é \033[1;31m{rodadas}\033[m\n") 
        
        #INFORMAR ERRO DE COMPARAÇÃO NO INPUT DO USUARIO
        erro = 0 
        
        #COMPARAR PALAVRA GERADA COM INPUT DO USUARIO
        for caracter in palavra: 
            if caracter in palpites: 
                    print(f"\033[0;34m{caracter}\033[m", end="")
            else: 
                    print("_", end = "")
                    erro += 1
        
        #VERIFICAR SE O USUARIO ERROU ALGUM CARACTER
        if erro == 0:
            print("\n")
            linha()
            print("VOCE VENCEU".center(40)) 
            print(f"A palavra é: {palavra}".center(40)) 
            break
        
        #INPUT DO USUARIO
        palpite = input("\n\nFaça um palpite: ")
        print("\n")
        
        #DEFINIR E NORMALIZAR ENTRADA DO USUARIO
        palpites += palpite.lower()
        
        #DIMINUIR CHANCES DO USUARIO
        if palpite not in palavra:
            rodadas -= 1
        
        #CRIAR SEPARADOR
        linha()
        
        #VERIFICAR QUANTIDADE DE RODADAS
        if rodadas == 0:
            print("Voce perdeu".center(40))
            print(f"A palavra é: {palavra}".center(40))
    
    #VERIFICAR ENCERAMENTO DO LOOP
    parar = input('\nDeseja encerrar o jogo?(s/n)')
    if parar.lower() == 's':
        break
    else:
        print("Gerando nova palavra.")