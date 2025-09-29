# Supposez que vous avez un fichier CSV nommé `ventes.csv` avec les colonnes 'Produit' et 'Revenu'.
# Écrivez le code Pandas pour lire ce fichier dans un DataFrame appelé `df`.
# (Vous n'avez pas besoin d'un vrai fichier, écrivez simplement le code).
# 💡 La fonction est `pd.read_csv('nom_fichier.csv')`.

import pandas as pd

df = pd.read_csv('assets/csv/ventes.csv')

print(df)
