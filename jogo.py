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

x = sample(lista,52)
i = 1
while i <= 52:
    print("{0}. {1}".format(i,x[i-1]))
    i += 1

print("")
b = input("Escolha uma carta (digite um número entre 1 e 52): ")
print("")
print("O estado atual do baralho é: ")


