import numpy as np
import math

t = np.arange(0, 5, 0.01)

X = []
for i in t:
    value = math.exp(-4*i)*(0.128*math.cos(9.16*i) + 1.12*math.sin(9.16*i)) + 0.052*math.sin(5*i) - 0.028*math.cos(5*i)
    X.append(value)
    
import matplotlib.pyplot as plt
plt.plot(t, X)
plt.title("Total Response for w = 5 rad/s")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("TR_Q2_W5")
plt.show()
