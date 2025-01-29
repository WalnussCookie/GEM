import numpy as np
import matplotlib.pyplot as plt

# Randwerte
u_eff_ideal = 230 #[V] Effektivwert der Spannung
p_ideal = 60 #[W] Glühlampenleistung  
i_hat_ideal =  p_ideal/u_eff_ideal*np.sqrt(2) #[A] Scheitelwert des Stroms (Berechnet aus Effektivwert von I für I sinusförmig)
f = 50 #[Hz] Netzfrequenz
T = 1/f * 1000 #[s] Periodendauer

# Messwerte
delta_t = np.array([1.4, 3.0, 4.8, 6.0, 7.4])
s_real = np.array([54.87, 51.31, 43.96, 36.86, 26.11])
p_real = np.array([52.98, 45.74, 30.51, 19.31, 7.44 ])
q_real = np.array([14.29, 23.25, 31.65, 31.39, 25.03])

def Time2Deg(dt):
    theta = dt * 360/T
    return theta

def Rad2Deg(theta):
    alpha = theta * 180/np.pi
    return alpha

def I_eff_theta(theta):
    i_eff_theta = i_hat_ideal/np.sqrt(2) * np.sqrt(1/np.pi * (np.pi - theta +1/2 * np.sin(2*theta)))
    return i_eff_theta

def Scheinleistung_ideal(theta):
    S = u_eff_ideal * I_eff_theta(theta)
    return S

def Wirkleistung_ideal(theta):
    P = u_eff_ideal*i_hat_ideal/(np.sqrt(2)*np.pi) * (np.pi-theta+1/2 * np.sin(2*theta))
    return P

def Blindleistung_ideal(S, P):
    Q = np.sqrt(S**2 - P**2)
    return Q

theta = np.linspace(0, np.pi-0.0001, 100) # Winkelvektor
theta_real = Time2Deg(delta_t) # Zündzeit in Radiant umrechnen

s_ideal = Scheinleistung_ideal(theta)
p_ideal = Wirkleistung_ideal(theta)
q_ideal = Blindleistung_ideal(s_ideal, p_ideal)

theta_ideal = Rad2Deg(theta)

plt.plot(theta_ideal, s_ideal, "--c",label="S-Theorie")
plt.plot(theta_ideal, p_ideal, "--m",label="P-Theorie")
plt.plot(theta_ideal, q_ideal, "--b",label="Q-Theorie")
#-------------------------------------------------------------
plt.plot(theta_real, s_real, "-cD",label="S-Messung")
plt.plot(theta_real, p_real, "-mo",label="P-Messung")
plt.plot(theta_real, q_real, "-bs",label="Q-Messung")
plt.xlim(0, 180)
plt.ylim(0, 65)
plt.xlabel("Zündwinkel ϑ in °")
plt.ylabel("Leistung  [W, VA, var]")
plt.legend(ncols=2)
plt.grid()
plt.savefig("Protokoll_5/Plots/Leistungskurve_Dimmer.pdf")
plt.show()
plt.close()
