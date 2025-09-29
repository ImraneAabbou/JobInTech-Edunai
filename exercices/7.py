# Importez `matplotlib.pyplot` en tant que `plt`.
# Tracez les données de ventes mensuelles : `mois = [1, 2, 3, 4]`, `ventes = [100, 120, 115, 130]`.
# Affichez le graphique en utilisant `plt.show()`.
# 💡 Utilisez `plt.plot(valeurs_x, valeurs_y)`.

import matplotlib.pyplot as plt

mois = [1, 2, 3, 4]
ventes = [100, 120, 115, 130]

plt.plot(mois, ventes)
plt.show()

