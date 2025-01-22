import numpy as np
import matplotlib.pyplot as plt

samplinRate = 24000
duration = 2
resolution = 14

u_mess, i_mess = np.load("Protokoll_5/Daten/Glühlampe.npy")

def Wandler(u_mess, i_mess):
    V_u = 10/566
    V_i = 10/0.9

    return u_mess/V_u, i_mess/V_i

t = np.linspace(0, duration, duration*samplinRate)

u, i = Wandler(u_mess, i_mess)

fig, ax1 = plt.subplots(tight_layout=True)
ax2 = ax1.twinx()

ax1.plot(t, u, "b", label="Spannung in V")
ax1.set_ylim(-360, 360)
ax1.tick_params(axis="y", labelcolor="b")

ax2.plot(t, i, "r", label="Spannung")
ax2.set_ylim(-0.5, 0.5)
ax2.tick_params(axis="y", labelcolor="r")


ax1.set_xlabel("Zeit in s")
ax1.set_ylabel("Spannung in V", color="b")
ax2.set_ylabel("Stromstärke in A", color="r")
ax1.set(title="Strom- und Spannungsverlauf über die Zeit")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.85))
#fig.tight_layout()

plt.show()                                       # Show the figure.
plt.close(fig)