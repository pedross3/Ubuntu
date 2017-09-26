"""def Fibonacci(val):
    a = [1,1]
    b = a[-1]
    t=0
    while t < val:
        b = b + a[-2]
        t+=1
        a.append(b)
    return a
    
print(Fibonacci(10))"""



list_a = ["a","b","c"]
list_b = [1,2,3]
def concatenation(a,b):
    new_list = []
    for i in a,b:
        new_list.append(a[i])
        new_list.append(b[i])
        print(new_list)
    return new_list
print(concatenation(list_a,list_b))
        
