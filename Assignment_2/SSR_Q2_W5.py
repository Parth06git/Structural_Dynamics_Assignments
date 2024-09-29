import numpy as np
import math

t = np.arange(0, 5, 0.01)

X = []
for i in t:
    value = 0.052*math.sin(5*i) - 0.028*math.cos(5*i)
    X.append(value)
    
import matplotlib.pyplot as plt
plt.plot(t, X)
plt.title("Steady State Response for w = 5 rad/s")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("SSR_Q2_W5")
plt.show()
