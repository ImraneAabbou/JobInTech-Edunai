# 1. Créez un DataFrame à partir des données clients.
# 2. Filtrez le DataFrame pour trouver tous les clients des 'USA' qui ont plus de 30 ans.
# 3. Calculez l'âge moyen de tous les clients.
# 4. Comptez combien de clients viennent de chaque pays.
#
# Données : `data = {'Nom': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 35, 40, 28], 'Pays': ['USA', 'Canada', 'USA', 'UK']}`
# 💡 Utilisez `&` pour plusieurs conditions de filtre. Utilisez `.mean()` pour la moyenne et `.value_counts()` pour le comptage.

import pandas as pd

data = {
    "Nom": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 35, 40, 28],
    "Pays": ["USA", "Canada", "USA", "UK"],
}
df = pd.DataFrame(data)

clients_usa_plus_30 = df[(df["Pays"] == "USA") & (df["Age"] > 30)]
print(clients_usa_plus_30)

age_moyen = df["Age"].mean()
print("Âge moyen:", age_moyen)

clients_par_pays = df["Pays"].value_counts()
print(clients_par_pays)
