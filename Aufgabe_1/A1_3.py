# -*- coding: utf-8 -*-
"""
Created on Mo Nov 5 2024

@author: Berenice Möhling
"""
# -------------------1.3-------------------
import os, re
import numpy as np 
import matplotlib.pyplot as plt 
import mdt

# globale Variablen
current_dir = os.path.dirname(__file__)            # aktueller Pfad
file_name = current_dir+"\\A1_3.npy"               # Pfad für die Datei mit den Messwerten
flag_go = False                                                 # Zustandsvariable für's Laden und arbeiten mit den Messwerten
# Initialisierungswerte für Messkarte
a=5
sR=48000
d=0.1
c=[0]
r=14
oT="volt"

############# Erzeugen der Messdaten #############
def get_Data():
    u_mess = mdt.dataRead(amplitude=a, samplingRate=sR, duration=d, channels=c, resolution=r, outType=oT)          # Aufnahme von Messwerten mit der Messkarte (Messbereich:+/- 5 V, Abtastrate: 48 kHz, Messdauer: 1 s, Auflösung: 14 bit)
    return u_mess

############# Exception Handling - Read File #############
try:                                                                                                                                                                            # Überprüfung, ob Datei vorhanden
    f = open(file_name)
    f.close()
except FileNotFoundError:                                                                                                                                       # Wenn keine Datei vorhanden ist, wird eine angelegt
    print("Datei existiert nicht."+" --- "+"Messwerte werden genereriert und gespeichert.\n")
    with open(file_name, "wb") as f_u:                                                                                                                       # Messwerte erzeugen und Speichern
        np.save(f_u, get_Data())
    print("\nMesswerte wurden gespeichert.")
    flag_go = True
else:
    try:                                                                                                                                                                        # Überprüfen, ob die vorhandene Datei Daten in der richtigen Form enthält
        content = open(file_name,"r")
        re.search(r'^\s*$', content.read())
    except UnicodeDecodeError:                                                                                                                               # Daten wurden gefunden
        content.close()
        print("Die Datei existiert und enthält Werte")
        flag_go = True
    else:                                                                                                                                                                      # Datei existiert, muss aber überschrieben werden
        content.close()
        print("Die Datei existiert, ist jedoch leer oder enthält falsche Werte."+" --- "+"Messwerte werden neu genereriert.\n")
        with open(file_name, "wb") as f_u:                                                                                                                   # Messwerte erzeugen und Speichern
            np.save(f_u, get_Data())
        print("\nMesswerte wurden gespeichert.")
        flag_go = True


 ############# Graphische Auswertung #############
if flag_go:
    with open(file_name, "rb") as f_u:                      
        u_value = np.load(f_u)
    #print(u_value)

    indices = np.arange(u_value.size)
    #print(indices)

    fig, ax = plt.subplots()                                                                                                            
    ax.scatter(indices, u_value[0,:], label="Spannungsverlauf")                              # Spannungskurve plotten
    
    p_ind = 860                                                                                                      # Index für ersten Nulldurchgang von u_value (markiert eventuell nicht den Nulldurchgang, für andere Messdaten)
    ax.plot(p_ind,u_value[0,p_ind], "ro")                                                                 # Start: eine Periode
    ax.plot(p_ind+960,u_value[0,p_ind+960], "ro")                                                # Ende: einer Periode (48kHz/50Hz=960 Messpunkte in einer Periode)

    plt.show()                                                                                                         # Show the figure.
    plt.close(fig)

    t = np.arange(0,d,1/sR)                                                                                  # Zeitvektor
    #t_two = np.linspace(0,d,int(d*sR), endpoint=False)                                     # Bei kleinen Samplingraten ungenau
    #print(t)
    
    fig_sp, axs = plt.subplots(2, 1, figsize=(8, 10), tight_layout=True)                 # Erzeugen einer Figur mit zwei Subplots

    # Plot 1 - gemessenes Signal
    axs[0].plot(t, u_value[0,:])
    axs[0].set(xlabel="Zeit t in s", ylabel="Spannung U in V")                         # Benennung der Achsen
    
    # Plot 2 - ausgeschnittenes Signal
    axs[1].plot(t[p_ind:p_ind+960], u_value[0,p_ind:p_ind+960])
    axs[1].set(xlabel="Zeit t in s", ylabel="Spannung U in V")                         # Benennung der Achsen

    axs[0].grid(True)
    axs[1].grid(True)

    plt.show()                                                                                                   # Show the figure.
    plt.close(fig_sp)