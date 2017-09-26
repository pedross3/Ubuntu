
##Write a function that checks whether an element occurs in a list.
a = [0,156,456462,3654,4,75,6,7,89]
def searchinlist(a,b):
    for t in a:
        if b == t:
            return b
print(searchinlist(a,5))


####Write a function that returns the elements on odd positions in a list.
##a = [0,1,2,3,4,5,6,7,8,9]
##
##def oddpositions(a):
##    lista = []
##    contagem = 0
##    for i in a:
##        if contagem%2==1:
##            lista.append(i)
##        contagem += 1
##    return lista
###return a[::2]
##    
##print(oddpositions(a))
##
##
##a = [0,1,2,3,4,5,6,7,8,9]
##def total (a):
##    n = 0
##    for t in a:
##        n = n + t
##    return n
##print(total(a))
##
##def palindrome_test(a):
##    if a[::-1] == a[::]:
##        return True
##    else:
##        return False
##a = [0,1,2,3,4,5,6,7,8,9]
##print(palindrome_test(a))
