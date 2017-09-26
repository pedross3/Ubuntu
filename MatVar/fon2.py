import matplotlib.pyplot as plt
import numpy as np


a = []
b = []
tempo1 = np.arange(-10,1,1)
tempo2 = np.arange(1,15,1)


for t in tempo1:
    t = t**5
    a.append(t)
    
    
for i in tempo2:
    i = i**2
    b.append(i)
    
    
plt.plot(tempo1, a)
plt.plot(tempo2, b)
plt.show()

