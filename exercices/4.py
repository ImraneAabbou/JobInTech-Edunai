# Créez un DataFrame à partir d'un dictionnaire de données de ventes : `{'Mois': ['Jan', 'Fév', 'Mar'], 'Ventes': [25000, 28000, 31000]}`.
# Affichez le DataFrame.
# 💡 Utilisez `pd.DataFrame(data_dict)`.

import pandas as pd

data = {'Mois': ['Jan', 'Fév', 'Mar'], 'Ventes': [25000, 28000, 31000]}
df = pd.DataFrame(data)
print(df)

