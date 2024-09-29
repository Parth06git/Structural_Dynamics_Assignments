import numpy as np
import matplotlib.pyplot as plt

m = 500  
c = 200  
k = 750  
F0 = 2000  
td = 9  
dt = 1  
tt = 12  

Wn = np.sqrt(k/m)
zeta = c / (2*np.sqrt(k*m))

t = np.arange(0, tt+dt, dt)

force = np.zeros_like(t)
force[t <= td] = F0

# Central Difference Method
x = np.zeros_like(t)
v = np.zeros_like(t)

x[0] = v[0] = 0

for i in range(1, len(t)-1):
    x[i+1] = (force[i] * dt**2 / m) + 2*x[i] - x[i-1] - (c * dt / m) * (x[i] - x[i-1]) - (k / m) * dt**2 * x[i]
    
# Theoretical Displacement
theoretical_disp = np.zeros_like(t)
for i, ti in enumerate(t):
    if ti <= td:
        theoretical_disp[i]=2.67*(1-np.cos(1.22*ti))
    else:
        theoretical_disp[i] = 2.67*(np.cos(1.22*(ti-td)-np.cos(1.22*ti)))

plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Numerical (Central Difference)', marker='o')
plt.plot(t, theoretical_disp, label='Theoretical', linestyle='--', marker='x')
plt.title('Response of Damped SDOF System')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()
plt.grid(True)
plt.savefig("Question_3_plot")
plt.show()