# Importez la bibliothèque Pandas en tant que `pd`.
# Créez une Série Pandas pour les prix des produits avec les produits comme index : `{'Ordinateur': 1200, 'Souris': 25, 'Clavier': 75}`.
# Affichez la série.
# 💡 Utilisez `pd.Series(data_dict)`.

import pandas as pd

prices = pd.Series({'Ordinateur': 1200, 'Souris': 25, 'Clavier': 75})
print(prices)
