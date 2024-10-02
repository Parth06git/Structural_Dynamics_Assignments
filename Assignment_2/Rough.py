# Code for finding Constant of Interpolation of Excitation Method

import numpy as np

# Define input parameters
zeta = 0.163  
omega_n = 1.22  
Delta_t = 1  
k = 750  

# Damped natural frequency
omega_D = omega_n * np.sqrt(1 - zeta**2)

# Coefficients
A = np.exp(-zeta * omega_n * Delta_t) * ((zeta / np.sqrt(1 - zeta**2)) * np.sin(omega_D * Delta_t) + np.cos(omega_D * Delta_t))

B = np.exp(-zeta * omega_n * Delta_t) * (1 / omega_D * np.sin(omega_D * Delta_t))

C = (1/k) * (2 * zeta / (omega_n * Delta_t) + np.exp(-zeta * omega_n * Delta_t) * (((1 - 2 * zeta**2) / (omega_D * Delta_t) - zeta / np.sqrt(1 - zeta**2)) * np.sin(omega_D * Delta_t) - (1 + 2 * zeta / (omega_n * Delta_t)) * np.cos(omega_D * Delta_t)))

D = (1/k) * (1 - 2 * zeta / (omega_n * Delta_t) + np.exp(-zeta * omega_n * Delta_t) * ((2 * zeta**2 - 1) / (omega_D * Delta_t) * np.sin(omega_D * Delta_t) + 2 * zeta / (omega_n * Delta_t) * np.cos(omega_D * Delta_t)))

A_prime = -np.exp(-zeta * omega_n * Delta_t) * (omega_n / np.sqrt(1 - zeta**2)) * np.sin(omega_D * Delta_t)

B_prime = np.exp(-zeta * omega_n * Delta_t) * (np.cos(omega_D * Delta_t) - (zeta / np.sqrt(1 - zeta**2)) * np.sin(omega_D * Delta_t))

C_prime = (1/k) * (1 / Delta_t - np.exp(-zeta * omega_n * Delta_t) * ((omega_n / np.sqrt(1 - zeta**2) + zeta / (Delta_t * np.sqrt(1 - zeta**2))) * np.sin(omega_D * Delta_t) + (1 / Delta_t) * np.cos(omega_D * Delta_t)))

D_prime = (1 / (k * Delta_t)) * (1 - np.exp(-zeta * omega_n * Delta_t) * ((zeta / np.sqrt(1 - zeta**2)) * np.sin(omega_D * Delta_t) + np.cos(omega_D * Delta_t)))

# Print results
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}")
print(f"A' = {A_prime}")
print(f"B' = {B_prime}")
print(f"C' = {C_prime}")
print(f"D' = {D_prime}")
