import numpy as np

i = 1
data_1 = [1.4, 3.817, 2.822, 10.4]
data_2 = [3.0, 3.817, 2.639, 8.98]
data_3 = [4.8, 3.812, 2.264, 5.99]
data_4 = [6.0, 3.812, 1.898, 3.79]
data_5 = [7.4, 3.817, 1.343, 1.46]

delta_t = eval(f"data_{i}[0]")
u_eff = 566/10 * eval(f"data_{i}[1]")
i_eff = 0.9/10 * eval(f"data_{i}[2]")
P_mess = 0.9*566/100 * eval(f"data_{i}[3]")

T = 20
theta = delta_t * 2*np.pi/T
theta_deg = delta_t * 360/T

i_hat = i_eff*np.sqrt(2)/np.sqrt(1/np.pi * (np.pi - theta +1/2*np.sin(2*theta)))

P = u_eff*i_hat/(np.sqrt(2)*np.pi)*(np.pi-theta+1/2*np.sin(2*theta))

S = u_eff*i_eff

Q = np.sqrt(S**2 - P_mess**2)

print("t:", delta_t)
print("U:", u_eff)
print("I:", i_eff)
print("P:", P_mess)
print("S:", S)
print("Q:", Q)
print("Theta:", theta_deg, "\n")
print(delta_t, u_eff, i_eff, P_mess, S, Q, theta_deg, "\n")
print(P)
print(P-P_mess)