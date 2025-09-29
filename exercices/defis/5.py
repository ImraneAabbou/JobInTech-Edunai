# 1. Créez un DataFrame à partir des données de ventes.
# 2. Groupez les données par 'Catégorie' et calculez les ventes totales pour chaque catégorie.
# 3. Créez un diagramme à barres montrant les ventes totales par catégorie.
# 4. Trouvez le prix moyen des produits dans la catégorie 'Électronique'.
#
# Données : 
# data = {
#   'Produit': ['Portable', 'Souris', 'Chemise', 'Jean'],
#   'Catégorie': ['Électronique', 'Électronique', 'Vêtements', 'Vêtements'],
#   'Ventes': [1200, 150, 200, 300]
# }
#
# 💡 Utilisez `.groupby('Catégorie')['Ventes'].sum()` pour l'agrégation. 
# Pour le filtrage et la moyenne, sélectionnez d'abord la catégorie, 
# puis calculez la moyenne de la colonne 'Ventes'.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Produit': ['Portable', 'Souris', 'Chemise', 'Jean'],
    'Catégorie': ['Électronique', 'Électronique', 'Vêtements', 'Vêtements'],
    'Ventes': [1200, 150, 200, 300]
}

df = pd.DataFrame(data)
ventes_totales = df.groupby('Catégorie')['Ventes'].sum()
ventes_totales.plot(kind='bar')
plt.title("Ventes totales par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Ventes")
plt.show()

moyenne_electronique = df[df['Catégorie'] == 'Électronique']['Ventes'].mean()
print("Prix moyen (Électronique):", moyenne_electronique)

