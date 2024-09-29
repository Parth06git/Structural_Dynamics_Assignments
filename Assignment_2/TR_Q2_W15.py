import numpy as np
import math

t = np.arange(0, 5, 0.01)

X = []
for i in t:
    value = math.exp(-4*i)*(0.12*math.cos(9.16*i) + 1.18*math.sin(9.16*i)) - 0.021*math.sin(15*i) - 0.02*math.cos(15*i)
    X.append(value)
    
import matplotlib.pyplot as plt
plt.plot(t, X)
plt.title("Total Response for w = 15 rad/s")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("TR_Q2_W15")
plt.show()
