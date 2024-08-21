# Given Information

m = 10 kg
k = 1000 N/m
x(0) = 0.1 m
$\hat{x}$(0) = 10 m/s

# Problem

1. Plot the undamped free vibration responce of the system.
2. Plot the damped free vibration of the system considering under-damped, critical damped and over-damped conditions.

# Solution of part - 1
```math
x(t) = x(0)cos(w_n*t) + ($\hat{x}$(0) \over w_n)sin(w_n*t)
```
where,

$w_{n}$ = $ \sqrt{k \over m} $

![plot](./Part_1_Plot.png)


Calculation and plotting is done in Part_a.py file.


