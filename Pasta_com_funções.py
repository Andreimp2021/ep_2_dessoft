def cria_baralho():

    lista = ["A♠" ,"K♠" ,"Q♠" ,"J♠" ,"10♠" ,"9♠" ,"8♠" ,"7♠" ,"6♠" ,"5♠" ,"4♠" ,"3♠" ,"2♠" ,"A♥" ,"K♥" ,"Q♥" ,"J♥" ,"10♥" ,"9♥" ,"8♥" ,"7♥" ,"6♥" ,"5♥" ,"4♥", "3♥" ,"2♥" ,"A♦" ,"K♦" ,"Q♦" ,"J♦" ,"10♦" ,"9♦" ,"8♦" ,"7♦" ,"6♦" ,"5♦" ,"4♦" ,"3♦" ,"2♦" ,"A♣" ,"K♣" ,"Q♣" ,"J♣" ,"10♣" ,"9♣" ,"8♣" ,"7♣" ,"6♣" ,"5♣" ,"4♣" ,"3♣" ,"2♣"]

    return lista 

def extrai_naipe(carta):
    if len(carta) <= 2:
        e = carta[1]
        return e
    elif len(carta) == 3:
        e = carta[2]
        return e

def extrai_valor(carta):
    if len(carta) == 2:
        e = carta[0]
        return e
    elif len(carta) == 3:
        e = carta[0] + carta[1]
        return e
        
def lista_movimentos_possiveis(lista, indice):
    lista2 = []
    if indice == 0:
        return []
    else:
        if extrai_naipe(lista[indice]) == extrai_naipe(lista[indice-1]) or  extrai_valor(lista[indice]) == extrai_valor(lista[indice-1]):
            lista2.append(1)

        if indice >= 3:
            if (extrai_naipe(lista[indice]) == extrai_naipe(lista[indice-3]) or  extrai_valor(lista[indice]) == extrai_valor(lista[indice-3])):
                lista2.append(3)

    return lista2
  
def empilha(baralho, o, d):
    o = int(o)
    d = int(d)
    baralho[d-1] = baralho[o-1]
    del baralho[o-1]
    return baralho

def extrai_valor(carta):
    if len(carta) == 2:
        e = carta[0]
        return e
    elif len(carta) == 3:
        e = carta[0] + carta[1]
        return e
        
def possui_movimentos_possiveis(lista):
    for indice in range(1,len(lista)):
        if extrai_naipe(lista[indice]) == extrai_naipe(lista[indice-1]) or  extrai_valor(lista[indice]) == extrai_valor(lista[indice-1]) or indice >= 3 and (extrai_naipe(lista[indice]) == extrai_naipe(lista[indice-3]) or  extrai_valor(lista[indice]) == extrai_valor(lista[indice-3])):
            return True

    else:
        return False


  


    