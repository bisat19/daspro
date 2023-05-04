#Nama : Abisatya Hastarangga Pradan
#NIM  : 24060122120004 

import ast
pasukan = ast.literal_eval(input())
from list_of_list import *

def max_list(L):
    if nb_elmt(L) <= 1:
        return L[0]
    elif not isinstance(firstList(L),list):
        maks = max_list(L[1:])
        if maks>L[0]:
            return maks
        else: 
            return L[0]

L = []
def ninja(S):
    if isEmptyLOL(S):
        return L
    else:
        if isList(firstList(S)):
            return ninja(tailList(S))
        elif isAtom(firstList(S)):
            L.append(firstList(S))
            ninja(tailList(S))
            return L
            
N = []
def remove_ninja(S):
    if isEmptyLOL(S):
        return N
    else:
        if isAtom(firstList(S)):
            return remove_ninja(tailList(S))
        elif isList(firstList(S)):
            N.append(firstList(S))
            remove_ninja(tailList(S))
            return N

Ninja = remove_ninja(pasukan)
Prajurit = ninja(pasukan)
Katon = Ninja[0]
Suiton = Ninja[1]
Doton = Ninja[2]
Raiton = Ninja[3]
Fuuton = Ninja[4]

print((max_list(Prajurit)+max_list(Katon)+
max_list(Suiton)+max_list(Doton)+max_list(Raiton)+max_list(Fuuton))*1000000)

