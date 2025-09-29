# 1. On vous donne les données de ventes pour deux régions différentes.
# 2. Tracez les ventes des deux régions sur le même graphique linéaire.
# 3. Ajoutez une légende pour distinguer 'Région A' et 'Région B'.
# 4. Ajoutez un titre et des étiquettes d'axes.
# 
# Données : `mois = [1, 2, 3, 4]`, `ventes_a = [100, 110, 130, 125]`, `ventes_b = [90, 105, 120, 135]`
# 💡 Appelez `plt.plot()` deux fois, une pour les données de chaque région. Utilisez le paramètre `label` dans `plt.plot()` puis appelez `plt.legend()`.

import matplotlib.pyplot as plt

mois = [1, 2, 3, 4]
ventes_a = [100, 110, 130, 125]
ventes_b = [90, 105, 120, 135]

plt.plot(mois, ventes_a, label='Région A')
plt.plot(mois, ventes_b, label='Région B')

plt.legend()

plt.show()

