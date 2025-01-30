import numpy as np
import matplotlib.pyplot as plt

# Messwerte
m_in_g = np.array([0, 50, 100, 150, 200, 250, 300])
m = m_in_g/1000
u_mess_viertel = np.array([-1.07, 113, 228, 340, 445, 557, 660]) #mV
u_mess_voll = np.array([0.18, 428, 864, 1297, 1735, 2157, 2577])

# Randwerte
k = 2.05
E = 70
h = 1           #mm
b = 50         #mm
l = 100        #mm
V = 2500    #V
g = 9.81     #m/s^2

def Viertelbruecke(m):
    beta = 4
    u = (6*k*l*m*g*V)/(E*b*beta*h**2)
    return u

def Vollbruecke(m):
    beta = 1
    u = (6*k*l*m*g*V)/(E*b*beta*h**2)
    return u

plt.plot(m_in_g, Viertelbruecke(m), "--b", label="Theorie")
plt.scatter(m_in_g, u_mess_viertel, s=10, c="r", marker="D", label="Messwerte", zorder=2)
plt.xlabel("Masse [g]")
plt.ylabel("Spannung [mV]")
plt.grid()
plt.legend()
plt.title("Kennlinie der Viertelbrücke")
plt.savefig("Protokoll_6/Plots/Viertelbruecke.pdf")
plt.show()                                       # Show the figure.
plt.close()                                     # Close the figure.


plt.plot(m_in_g, Vollbruecke(m), "--b", label="Theorie")
plt.scatter(m_in_g, u_mess_voll, s=10, c="r", marker="D", label="Messwerte", zorder=2)
plt.xlabel("Masse [g]")
plt.ylabel("Spannung [mV]")
plt.grid()
plt.legend()
plt.title("Kennlinie der Vollbrücke")
plt.savefig("Protokoll_6/Plots/Vollbruecke.pdf")
plt.show()                                       # Show the figure.
plt.close()                                     # Close the figure.