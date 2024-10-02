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
Wd = Wn*np.sqrt(1-zeta**2)

t = np.arange(0, tt+dt, dt)

force = np.zeros_like(t)
force[t <= td] = F0

# Central Difference Method
p = []
x = []
u_prev = 2
x.append(0)
p.append(force[0] - 400*u_prev + 250*x[0])
x.append(p[0]/600)
for i in range(1, len(t)-1):
    p.append(force[i] - 400*x[i-1] + 250*x[i])
    x.append(p[i]/600)


# Interpolation of Excitation Method
A = 0.42
B = 0.63
C = 0.0005
D = 0.0003
A1 = -0.94
B1 = 0.168
C1 = 0.0005
D1 = 0.0008
u = []
v = []
u.append(0)
v.append(0)

for i in range(0, len(t)-1):
    u.append(A*u[i] + B*v[i] + C*force[i] + D*force[i+1])
    v.append(A1*u[i] + B1*v[i] + C1*force[i] + D1*force[i+1])

# Theoretical Displacement
theoretical_disp = []
for i, ti in enumerate(t):
    when = 0
    if ti <= td:
        theoretical_disp.append((F0/k)*(1 - np.exp(-zeta*Wn*ti)*(np.cos(Wd*ti) + (zeta/np.sqrt(1-zeta**2))*np.sin(Wd*ti))))
        if ti == td:
            when = i
            print(theoretical_disp[when])
    else:
        theoretical_disp.append(np.exp(-0.2*(ti-td)) * (2.79*np.cos(Wd*(ti-td)) + 0.01583*np.sin(Wd*(ti-td))))

plt.figure(figsize=(10, 6))
plt.plot(t, u, label='Numerical (Interpolation of Excitation)', marker='+')
plt.plot(t, x, label='Numerical (Central Difference)', linestyle='-.', marker='o')
plt.plot(t, theoretical_disp, label='Theoretical', linestyle='--', marker='x')
plt.title('Response of Damped SDOF System')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()
plt.grid(True)
plt.savefig("Question3_plot")
plt.show()