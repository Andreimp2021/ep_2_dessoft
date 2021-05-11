from math import sqrt
import Pasta_com_funções
from random import sample
  
print("Paciência Acordeão")
print("==================") 
print("")
print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.") 
print("")
print("Existem apenas dois movimentos possíveis:") 
print("")
print("1. Empilhar uma carta sobre a carta imediatamente anterior;") 
print("2. Empilhar uma carta sobre a terceira carta anterior.") 
print("")
print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:") 
print("")
print("1. As duas cartas possuem o mesmo valor ou") 
print("2. As duas cartas possuem o mesmo naipe.") 
print("")
print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.")
print("")
input("Aperte [Enter] para iniciar o jogo...")
print("")
print("O estado atual do baralho é: ")
print("")

lista = ["A♠" ,"K♠" ,"Q♠" ,"J♠" ,"10♠" ,"9♠" ,"8♠" ,"7♠" ,"6♠" ,"5♠" ,"4♠" ,"3♠" ,"2♠" ,"A♥" ,"K♥" ,"Q♥" ,"J♥" ,"10♥" ,"9♥" ,"8♥" ,"7♥" ,"6♥" ,"5♥" ,"4♥", "3♥" ,"2♥" ,"A♦" ,"K♦" ,"Q♦" ,"J♦" ,"10♦" ,"9♦" ,"8♦" ,"7♦" ,"6♦" ,"5♦" ,"4♦" ,"3♦" ,"2♦" ,"A♣" ,"K♣" ,"Q♣" ,"J♣" ,"10♣" ,"9♣" ,"8♣" ,"7♣" ,"6♣" ,"5♣" ,"4♣" ,"3♣" ,"2♣"]

baralho = sample(lista,52)
i = 1
while i <= 52:
    print("{0}. {1}".format(i,baralho[i-1]))
    i += 1

print("")
indice = input("Escolha uma carta (digite um número entre 1 e 52): ")

lista2 = []

while Pasta_com_funções.possui_movimentos_possiveis(lista) == True:
    while int(indice) > len(baralho) or int(indice) < 1:
        indice = input("Posição inválida. Por favor, digite um número entre 1 e {0}: ".format(len(baralho)))
    
    indice = int(indice)
    movimento = True
    while movimento == True:
        print(Pasta_com_funções.lista_movimentos_possiveis(baralho,indice))
        if Pasta_com_funções.lista_movimentos_possiveis(baralho, indice) == [1]:
            destino = indice-1
            baralho = Pasta_com_funções.empilha(baralho,indice, destino)
            movimento = False

        elif Pasta_com_funções.lista_movimentos_possiveis(baralho, indice) == [3]:
            destino = indice-3
            baralho = Pasta_com_funções.empilha(baralho,indice, destino)
            movimento = False

        elif Pasta_com_funções.lista_movimentos_possiveis(baralho, indice) ==  [1 ,3]:
            pergunta = int(input("Sobre qual carta você quer empilhar o {0}?\n 1. {1}\n 2.{2} ".format(baralho[indice-1], baralho[indice-2], baralho[indice-4])))
            while pergunta != 1 or pergunta != 2:
                pergunta = int(input("Opção inválida. Sobre qual carta você quer empilhar o {0}?\n 1. {1}\n 2.{2} ".format(baralho[indice-1], baralho[indice-2], baralho[indice-4])))
            if pergunta == 1:
                destino = indice-2
                baralho = Pasta_com_funções.empilha(baralho,indice, destino)
            elif pergunta == 2:
                destino = indice-4
                baralho = Pasta_com_funções.empilha(baralho,indice,destino)

        else:
            indice = int(input("A carta {0} não pode ser movida, insira outro número.".format(baralho[indice-1])))

print("você perdeu :(")

  


