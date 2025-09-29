# Créez un diagramme à barres pour l'inventaire des produits : `produits = ['Portables', 'Souris', 'Claviers']`, `stock = [50, 200, 150]`.
# 💡 Utilisez `plt.bar(valeurs_x, valeurs_y)`.

import matplotlib.pyplot as plt

produits = ['Portables', 'Souris', 'Claviers']
stock = [50, 200, 150]

plt.bar(produits, stock)
plt.show()

