from curses.ascii import NUL
from random import choice
import os

entradas_erradas = []
tentativas = []
palavra_finalizada = []
erros = [("""
   |-------
   |      |
   |    
   |    
   |    
   |     
   |     
___|___ 
"""),("""
   |-------
   |      |
   |      _
   |     |_|
   |      
   |     
   |     
___|___ 
"""),( """
   |-------
   |      |
   |      _
   |     |_|
   |      |
   |      |
   |     
___|___ 
"""),( """
   |-------
   |      |
   |      _
   |     |_|
   |    --|
   |      |
   |     
___|___ 
"""),( """
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     
___|___ 
"""),("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     / 
___|___ 
"""),("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     / \\
___|___ 
""")]

def selecionar_palavra():
    palavras = []
    with open("frutas.txt", "r") as frutas:
        list_frutas = frutas.read()
        palavras = list_frutas.split("\n")
    palavra = choice(palavras)
    return palavra.upper()


def valida_entrada(palavra: str, entrada: str):
    palavra_finalizada.clear()
    if not entrada in palavra:
        entradas_erradas.append(entrada)
    else:
        tentativas.append(entrada)
    for letra in palavra:
        if letra in tentativas:
            print(letra, end=" ")
            palavra_finalizada.append(letra)
        else:
            print("_", end=" ")
        


def limpa_terminal():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def apresentar(palavra:str, acerto:bool):
    if acerto == True:
        print('*'*32)
        print(' PARABÉNS VOCÊ ACERTOU A PALAVRA! ')
        print(f" A PALAVRA DA VEZ ERA: {palavra} ")
        print('*'*32)
    else:
        print('*'*32)
        print(' INFELIZMENTE VOCÊ ERROU A PALAVRA! ')
        print(f" A PALAVRA DA VEZ ERA: {palavra} ")
        print('*'*32)
        
        
def main():
    joga_novamente = False
    
    print("=" * 42)
    print(" BEM VINDO AO JOGO DA FORCA DA LET'S CODE\n  Tente acertar a palavra para salvar a\n \t\tADA")
    print("=" * 42)
    input("\n\tVocê está Pronto?\n   Precione Entre para continuar")
    
    while not joga_novamente:
        end = False
        palavra = selecionar_palavra()
        
        entradas_erradas.clear()
        tentativas.clear()
        
        while not end:
            limpa_terminal()
            cont = 1
            
            if len(entradas_erradas)>=0:
                print("Dica: Fruta")
                if len(entradas_erradas) == 6:
                    apresentar(palavra, False)
                    end = True
                    break
                else:
                    print(erros[len(entradas_erradas)])
                    if cont == 1:
                        valida_entrada(palavra, '')
                        cont = 2
                        print('\n')
            
            print(f"Entradas Incorretas {entradas_erradas}\n")
            
            entrada = str(input("ENTRE COM A LETRA: "))
            entrada = entrada.upper()
            
            
            valida_entrada(palavra, entrada)
            print('\n')
            
            palavra_completa = ''.join(palavra_finalizada)
            
            if palavra_completa == palavra:
                 limpa_terminal()
                 apresentar(palavra, True)
                 end = True
                 break
            
              
        joga = input("GOSTARIA DE JOGAR NOVAMENTE? \n SIM OU NÃO: ")
        if joga.upper() == "NAO" or joga.upper() == 'NÃO':
            joga_novamente = True


main()
