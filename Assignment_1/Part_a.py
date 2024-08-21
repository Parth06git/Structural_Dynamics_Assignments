import numpy as np
import math

m = 10
k = 1000
x = 0.1
dx = 10

W_n = math.sqrt(k/m)
T_n = (2*math.pi)/W_n

t = np.arange(0, 3*T_n, 0.01)

X = []
for i in t:
    value = x*math.cos(W_n*i) + (dx/W_n)*math.sin(W_n*i)
    X.append(value)
    
import matplotlib.pyplot as plt
plt.plot(t, X)
plt.title("Undamped Free vibration of the system")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("Part_1_Plot")
plt.show()
