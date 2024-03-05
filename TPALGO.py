#MUJINGA KAJOBA
#ABONGI lindembu


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Définition de la fonction pour le système mécanique
def systeme_mecanique(x, t, m, k, alpha, F):
    x1, x2 = x[0], x[1]  # x1 représente la position, x2 représente la vitesse
    dx1_dt = x2
    dx2_dt = (F - alpha * x2 - k * x1) / m  # équation différentielle du système

    return [dx1_dt, dx2_dt]


# Paramètres du système
m = 10  # masse en kg
k = 4000  # constante de raideur du ressort en N/m
alpha = 20  # coefficient de frottement en Ns/m

# Cas a) Oscillations libres avec F(t) = 0
F = 0  # force extérieure nulle

# Conditions initiales
x0 = 0.01  # position initiale en m
v0 = 0  # vitesse initiale en m/s
initial_conditions = [x0, v0]

# Temps
t = np.linspace(0, 10, 100)  # intervalle de temps de 0 à 10 secondes

# Résolution de l'équation différentielle du système
solution_a = odeint(systeme_mecanique, initial_conditions, t, args=(m, k, alpha, F))
x_a = solution_a[:, 0]  # position

# Calcul des énergies
Ep = 0.5 * k * x_a ** 2  # énergie potentielle
Ec = 0.5 * m * solution_a[:, 1] ** 2  # énergie cinétique
Em = Ep + Ec  # énergie mécanique

# Tracé des graphiques pour le cas a)
plt.figure()
plt.plot(t, x_a)
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.title('Réponse du système mécanique - Cas a)')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(t, Ep, label='Ep')
plt.plot(t, Ec, label='Ec')
plt.plot(t, Em, label='Em')
plt.xlabel('Temps (s)')
plt.ylabel('Énergie (J)')
plt.title('Énergies du système mécanique - Cas a)')
plt.legend()
plt.grid(True)
plt.show()


# Cas b) Force extérieure F(t) = F0 * cos(ωt)
F0 = 100  # amplitude de la force en N
omega = 10  # fréquence de la force en rad/s

# Résolution de l'équation différentielle du système pour le cas b)
solution_b = odeint(systeme_mecanique, initial_conditions, t, args=(m, k, alpha, F0 * np.cos(omega * t)))
x_b = solution_b[:, 0]  # position

# Tracé de la réponse totale x en fonction du temps pour le cas b)
plt.figure()
plt.plot(t, x_b)
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.title('Réponse du système mécanique - Cas b)')
plt.grid(True)
plt.show()