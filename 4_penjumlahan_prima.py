#Nama : Abisatya Hastarangga Pradan
#NIM  : 24060122120004 

import ast
list_of_list = ast.literal_eval(input())
from list_of_list import*

def IsPrima(n,i=2):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2 == 0:
        return False
    elif i*i > n:
        return True
    else:
        return IsPrima(n,i+1)



def penjumlahan_prima(S):
    if isEmptyLOL(S):
        return 0
    else:
        if isAtom(firstList(S)):
            if IsPrima(firstList(S)):
                return firstList(S) + penjumlahan_prima(tailList(S))
            else:
                return 0 + penjumlahan_prima(tailList(S))
        elif isList(firstList(S)):
            return penjumlahan_prima(firstList(S)) + penjumlahan_prima(tailList(S))

print(penjumlahan_prima(list_of_list))