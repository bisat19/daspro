#Nama : Abisatya Hastarangga Pradan
#NIM  : 24060122120004 

import ast
list_of_list = ast.literal_eval(input())
from list_of_list import*

def penjumlahan_ganjil(S):
    if isEmptyLOL(S):
        return 0
    else:
        if isAtom(firstList(S)):
            if firstList(S) % 2 != 0:
                return firstList(S) + penjumlahan_ganjil(tailList(S))
            else:
                return penjumlahan_ganjil(tailList(S))
        elif isList(firstList(S)):
            return penjumlahan_ganjil(firstList(S)) + penjumlahan_ganjil(tailList(S))

print(penjumlahan_ganjil(list_of_list))