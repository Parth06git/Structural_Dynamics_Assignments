import numpy as np
import math

m = 10
k = 1000

W_n = math.sqrt(k/m)
T_n = (2*math.pi)/W_n

t = np.arange(0, 3*T_n, 0.01)

X = []
for i in t:
    value = 0.1*math.cos(W_n*i) + 1.06*math.sin(W_n*i) -0.04*math.sin(15*i)
    X.append(value)
    
import matplotlib.pyplot as plt
plt.plot(t, X)
plt.title("Total Response for w = 15 rad/s")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("TR_Q1_W15")
plt.show()
