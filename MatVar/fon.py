import matplotlib.pyplot as plt


a = []
x = []
b = 0
for e in range (1,10000):
    a.append(e)
    x.append(b)
    e = e**2
    b += 1
plt.plot(x,a)
plt.grid()
plt.show()
