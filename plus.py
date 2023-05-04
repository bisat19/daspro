def plus(x,y):
    if y == 0:
        return x
    else :
        return 1 + plus(x, y-1)

print(plus(2,3))

