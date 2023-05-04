#Nama : Abisatya Hastarangga Pradan
#NIM  : 24060122120004 

import ast
LOL = ast.literal_eval(input())
ang = int(input())
from list_of_list import*

def hindari_monster(S,n):
    if isEmptyLOL(S):
        return S
    else:
        if isAtom(firstList(S)):
            if firstList(S) % n == 0 :
                return hindari_monster((tailList(S)),n)
            else:
                return [firstList(S)] + hindari_monster((tailList(S)),n)
        elif isList(firstList(S)):
            return [hindari_monster(firstList(S),n)] + hindari_monster(tailList(S),n)


print(hindari_monster(LOL,ang))
