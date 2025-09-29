# 1. Créez un DataFrame Pandas à partir du dictionnaire de données de ventes fourni.
# 2. Calculez le revenu total pour le mois.
# 3. Trouvez le produit avec le revenu le plus élevé et affichez son nom et son revenu.
# 4. Ajoutez une nouvelle colonne 'Bénéfice' qui correspond à 20% du 'Revenu'.
#
# Données : `data = {'Produit': ['A', 'B', 'C', 'D'], 'Unités Vendues': [100, 150, 80, 120], 'Prix': [10, 12, 15, 11]}`
# 💡 Créez d'abord une colonne 'Revenu' (`Unités Vendues` * `Prix`). Ensuite, utilisez `.sum()`, `.idxmax()`, et la création de colonne de base.

import pandas as pd

data = {
    "Produit": ["A", "B", "C", "D"],
    "Unités Vendues": [100, 150, 80, 120],
    "Prix": [10, 12, 15, 11],
}
df = pd.DataFrame(data)

df["Revenu"] = df["Unités Vendues"] * df["Prix"]
total_revenu = df["Revenu"].sum()
print("Revenu total:", total_revenu)

idx_max = df["Revenu"].idxmax()
print(
    "Produit avec le revenu le plus élevé:",
    df.loc[idx_max, "Produit"],
    "Revenu:",
    df.loc[idx_max, "Revenu"],
)

df["Bénéfice"] = df["Revenu"] * 0.2
print(df)
