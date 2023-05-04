#Nama : Abisatya Hastarangga Pradan
#NIM  : 24060122120004 

import ast
list_of_list = ast.literal_eval(input())
from list_of_list import*

def jumlahkartu(S):
    if isEmptyLOL(S):
        return 0
    else:
        if isAtom(firstList(S)):
            return 1 + jumlahkartu(tailList(S))
        else:
            return jumlahkartu(firstList(S)) + jumlahkartu(tailList(S))

print(jumlahkartu(list_of_list))

def nbelm(S):
    count = 0
    for elem in S:
        if type(elem) == list:
            count += nbelm(elem)
        else:
            count += 1
    return count

#print(nbelm(list_of_list))