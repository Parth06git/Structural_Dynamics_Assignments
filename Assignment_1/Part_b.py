import numpy as np
import math

m = 10
k = 1000
W_n = math.sqrt(k/m)
T_n = (2*math.pi)/W_n
C_cr = 2*math.sqrt(k*m)

t = np.arange(0, 3.5*T_n, 0.01)

X_ud = []
X_od = []
X_cr = []

# For Under-damped condition
c = 60
ξ = c/C_cr
W_d = W_n*math.sqrt(1 - (ξ*ξ))

for i in t:
    value = 0.1*math.exp(-(c*i)/(2*m))*math.cos(W_d*i) + 1.08*math.exp(-(c*i)/(2*m))*math.sin(W_d*i)
    
    X_ud.append(value/0.1)

# For Over-damped condition
c = 450
ξ = c/C_cr
r1 = W_n*(-ξ + math.sqrt((ξ*ξ) - 1))
r2 = W_n*(-ξ - math.sqrt((ξ*ξ) - 1))

for i in t:
    value = 0.35*math.exp(r1*i) - 0.25*math.exp(r2*i)
    X_od.append(value/0.1)

# For Critical condition
c= C_cr
ξ = c/C_cr

for i in t:
    value = math.exp(-W_n*i)*(0.1 + 11*i)
    X_cr.append(value/0.1)    

import matplotlib.pyplot as plt
plt.plot(t/T_n, X_ud, color = 'grey', label = 'Under-damped, ξ = 0.3')
plt.plot(t/T_n, X_od, color = 'yellow', label = 'Over-damped, ξ = 2.25')
plt.plot(t/T_n, X_cr, color = 'blue', label = 'Critical-damped, ξ = 1')
plt.legend()
plt.title("Undamped Free vibration of the system")
plt.xlabel("t/Tn")
plt.ylabel("x(t)/x(0)")
plt.savefig("Part_2_Plot")
plt.show()