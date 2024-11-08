# -*- coding: utf-8 -*-
"""
Created on Mo Nov 6 2024

@author: Berenice Möhling
"""
# -------------------1.3-------------------
import numpy as np 
import matplotlib.pyplot as plt 
#                                        
# 35*m+n = 0.45   =>      | 35    1 |  | m | = | 0.45 |
#   0*m+n = 3.1                |   0    1 |  |  n |    | 3.1   |   
#                                       

coeff_matrix = np.array([[35, 1],[0,1]])                                            # Koeffizientenmatrix des Linearen Gleichungssystems
v_vector = np.array([0.45, 3.1])                                                       # Spannungsvektor des LGS
coefficient = np.matmul(np.linalg.inv(coeff_matrix), v_vector)       # Vektor mit Koeffizienten m und n
#print(coefficient)

def angle2voltage(angle):
    voltage = coefficient[0]*angle+coefficient[1]            # Umrechnung von Winkel zu Spannung
    return voltage

print(angle2voltage(0))
print(angle2voltage(35))
t = np.linspace(0,10, 100)                                              # Zeitvektor
angle_t = 0.5*(np.tanh(t-5)+1)*35                                # Winkelfunktion
#print(angle2voltage(angle_t))

# Plot
fig, ax1 = plt.subplots(tight_layout=True)

# Graph Winkel
ax1.set_xlabel("Zeit in s")
ax1.set_ylabel("Winkel in °", color="b")
ax1.plot(t, angle_t, "b", label="Winkel")
ax1.tick_params(axis="y", labelcolor="b")

# Graph Spannung
ax2 = ax1.twinx()
ax2.set_ylabel("Spannung in V", color="r")
ax2.plot(t, angle2voltage(angle_t), "r", label="Spannung")
ax2.tick_params(axis="y", labelcolor="r")

ax1.grid(True)
ax1.set(title="Winkel- und Spannungsverlauf über die Zeit")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.85))
#fig.tight_layout()

plt.show()                                       # Show the figure.
plt.close(fig)

