# En utilisant le DataFrame de l'exercice précédent, sélectionnez et affichez uniquement la colonne 'Ventes'.
# 💡 Vous pouvez sélectionner une colonne en utilisant `df['NomColonne']`.

import pandas as pd

data = {'Mois': ['Jan', 'Fév', 'Mar'], 'Ventes': [25000, 28000, 31000]}
df = pd.DataFrame(data)
print(df['Ventes'])

