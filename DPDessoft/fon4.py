##def arimethicproggression(a,target, initial):
##    for t in range(target+1):
##        initial = initial + (a)
##        if initial == target:
##            return initial
##        
##def geometricproggression(q,target,initial):
##    for t in range(target+1):
##        initial = initial*q
##        if initial== target:
##            return initial

"""Write three functions that compute the sum of the
numbers in a list: using a for-loop, a while-loop
and recursion. (Subject to availability of these
constructs in your language of choice.)"""
a = [0,1,2,3,4,5,6,7,8,9]
def summa (a):
    n = 0
    t = 0
    while t < len(a):
        n = n + a[t]
        t = t + 1
        print(n)
    return n
print(summa(a))
