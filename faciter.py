def faciter (n,count,hasil):
    if n == count:
        return hasil*count
    else:
        return faciter(n, count+1, hasil*count)
    
print(faciter())