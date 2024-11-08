# -*- coding: utf-8 -*-
"""
Created on Mo Nov 4 2024

@author: Berenice Möhling
"""
# -------------------1.2-------------------
import numpy as np

# -1.-
x = np.linspace(1, 1000, 1000)                    # Erzeugen von Vektor x (Variante 1)
#print("\n", x)

x = np.arange(1, 1001)                              # Erzeugen von Vektor x (Variante 2)
#print("\n", x)

# -2.-
new_x = x[9:50]                                       # Ausschneiden der Elemente 10-50 aus x und Zuordnung dieser zu einem neuen Vektor
#print("\n", new_x)

# -3.-
new_x[0] = 0                                            # Änderung des Vektors new_x bewirkt eine Änderung des Vektor x
#print("\n", new_x)
#print("\n", x[10])                                      

# -4.-
y = np.linspace(0.2, 200, 1000)               # Erzeugen von Vektor y
#print("\n", y)

#print("\n", np.dot(x, y))                           # Skalarprodukt von x und y

# -5.-
#print("\n", np.multiply(x, y))                   # Elementweise Multiplikation von x und y

# -6.-
#print("\n", np.sum(x))                             # Summierung aller Elemente von x ohne Schleife

# -7.-
rand_array = np.random.rand(3, 4)         # Erzeugen einer 3x4 Matrix mit gleichverteilten Zufallszahlen zwischen 0 und 1 (Variante 1, immer zwischen 0 und 1)
#print("\n", rand_array)

rand_array_two = np.random.uniform(0,1, (3, 4))         # Erzeugen einer 3x4 Matrix mit gleichverteilten Zufallszahlen zwischen 0 und 1 (Variante 2, Zufallszahlen-Bereich ist veränderlich)
#print("\n", rand_array_two)

# -8.-
rand_array = np.vstack((rand_array, np.ones_like(rand_array, shape=4)))         # Hinzufügen einer weiteren Zeile, welche nur Einsen enthält (angepasst ans Format der Matrix)
#print("\n", rand_array)

# -9.-
#print("\n", np.transpose(rand_array))     # Transponierte der Matrix rand_array (mit generischer Funktion)

#print("\n", np.linalg.inv(rand_array))      # Inverse der Matrix rand_array

#print("\n", np.linalg.det(rand_array))      # Determinante der Matrix rand_array

# -10.-
# Sinusförmige Wechselspannung: U(t) = û*sin(2*pi*f*t) mit t = [0;T], T= 1/f
f = 50                      # [f] = Hz
T = 1/f * 1000         # [T] = ms
au = 5                     # [au] = V

t = np.linspace(0, T, 30)      # Vektor mit den Zeitwerten für eine Periode
print("\n", t)

y_u = au*np.sin(2*np.pi*1/T*t)        # Vektor mit den zeitlich veränderlichen Spannungswerten
print("\n", y_u)

# -11.-
import matplotlib.pyplot as plt
import os

# Get the current working directory
current_dir = os.path.dirname(__file__)

fig, ax = plt.subplots()                                                                                                            # Create a figure containing a single Axes.
ax.plot(t, y_u,  label="Spannungsverlauf")                                                                             # Spannungskurve plotten
ax.set(title="Spannungsverlauf", xlabel="Zeit t in ms", ylabel="Spannung U in V")             # Benennung der Achsen und des Plots

# -12.-
ind_max = np.argmax(y_u)                                                         # Bestimmen des Indexes des Maximalwertes von y_u

ax.plot(t[ind_max], y_u[ind_max], "ro", label="Maximum")        # Markierung des Maximums
ax.legend()                                                                                  # Legende

fig.savefig(current_dir+"\\Spannung.png", dpi=fig.dpi)              # Speicher der Grafik als PNG

#plt.show()                                                                                    # Show the figure.

plt.close(fig)                                                                                # Schließen der Figur

# -13.-
with open(current_dir+"\\Test_t.npy", "wb") as f_t:                      # Speichern von t und y_u in je einer Datei
    np.save(f_t, t)
with open(current_dir+"\\Test_u.npy", "wb") as f_u:
    np.save(f_u, y_u)

with open(current_dir+"\\Test_t.npy", "rb") as f_t:                       # Laden von t und y_u aus je einer Datei
    a = np.load(f_t)
with open(current_dir+"\\Test_u.npy", "rb") as f_u:
    b = np.load(f_u)

#print("\n", a, "\n", b)

# -14.-
fig_a, axs = plt.subplots(2, 1, figsize=(8, 10), tight_layout=True)

# Plot 1
axs[0].plot(t, y_u,  label="Spannungsverlauf")                                               # Spannungskurve plotten
axs[0].set(xlabel="Zeit t in ms", ylabel="Spannung U in V")                         # Benennung der Achsen

# Plot 2
axs[1].plot(t, np.random.rand(30),  label="Rauschen")                                 # Rauschen plotten
axs[1].set(xlabel="Zeit t in ms", ylabel="Spannung U in V")                        # Benennung der Achsen

# -15.-
fig_a.savefig(current_dir+"\\Spannung_Rauschen.pdf", dpi=fig.dpi)            # Speicher der Grafik als PDF

plt.show()                                                                                                     # Show the figure.
