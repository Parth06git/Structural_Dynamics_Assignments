import numpy as np
import math

W_n = 15
T_n = (2*math.pi)/W_n

t = np.arange(0, 3*T_n, 0.01)

X = []
for i in t:
    value = -0.04*math.sin(15*i)
    X.append(value)
    
import matplotlib.pyplot as plt
plt.plot(t, X)
plt.title("Steady State Response for w = 15 rad/s")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("SSR_Q1_W15")
plt.show()
