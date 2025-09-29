# En utilisant le graphique de l'exercice précédent, ajoutez un titre 'Tendance des Ventes Mensuelles'.
# Ajoutez une étiquette pour l'axe des x 'Mois' et pour l'axe des y 'Ventes (€)'.
# 💡 Utilisez `plt.title()`, `plt.xlabel()`, et `plt.ylabel()` avant `plt.show()`.

import matplotlib.pyplot as plt

mois = [1, 2, 3, 4]
ventes = [100, 120, 115, 130]

plt.plot(mois, ventes)
plt.title('Tendance des ventes mensuelles')
plt.xlabel('Mois')
plt.ylabel('Ventes (€)')
plt.show()

