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
    if len(carta) <= 1:
        e = carta[1]
        return e
    elif len(carta) == 3:
        e = carta[0] + carta[1]
        return e 

blablabla