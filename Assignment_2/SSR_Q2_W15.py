import numpy as np
import math

t = np.arange(0, 3, 0.01)

X = []
for i in t:
    value = - 0.021*math.sin(15*i) - 0.02*math.cos(15*i)
    X.append(value)
    
import matplotlib.pyplot as plt
plt.plot(t, X)
plt.title("Total Response for w = 15 rad/s")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("SSR_Q2_W15")
plt.show()
