# En utilisant le DataFrame des ventes, filtrez et affichez uniquement les lignes où les 'Ventes' sont supérieures à 29000.
# 💡 La syntaxe pour filtrer est `df[df['NomColonne'] > valeur]`.

import pandas as pd

data = {'Mois': ['Jan', 'Fév', 'Mar'], 'Ventes': [25000, 28000, 31000]}
df = pd.DataFrame(data)
print(df[df['Ventes'] > 29000])

