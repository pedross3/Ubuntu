import matplotlib.pyplot as plt
c=1
for t in range(1,100):
    a=[]
    b = ((-1)**t)/t
    a.append(b)
    c+=1
plt.plot(a,t,'ro')
plt.grid()
plt.show()
