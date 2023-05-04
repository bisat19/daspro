#Nama : Abisatya Hastarangga Pradan
#NIM  : 24060122120004 

import ast
permen = ast.literal_eval(input())
from list_of_list import *

def penjumlahanlist(S):
    if isEmptyLOL(S):
        return 0
    else:
        if isAtom(firstList(S)):
            return firstList(S) + penjumlahanlist(tailList(S))
        elif isList(firstList(S)):
            return penjumlahanlist(firstList(S)) + penjumlahanlist(tailList(S))

def belipermen(S):
    if isEmptyLOL(S):
        return 0
    else:
        if isAtom(firstList(S)):
            if firstList(S)%2 == 0:
                return firstList(S)*4000 + belipermen(tailList(S))
            else:
                return firstList(S)*3000 + belipermen(tailList(S))
        elif isList(firstList(S)):
            if penjumlahanlist(firstList(S))%2 == 0:
                return penjumlahanlist((firstList(S)))*2000 + belipermen(tailList(S))
            else:
                return penjumlahanlist((firstList(S)))*1000 + belipermen(tailList(S))

print(belipermen(permen))
