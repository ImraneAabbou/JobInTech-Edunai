# Créez un tableau NumPy de nombres de 1 à 5.
# Multipliez le tableau entier par 2 et affichez le résultat.
# Ajoutez 10 au tableau entier et affichez le résultat.
# 💡 Les opérations vectorisées de NumPy vous permettent de faire `mon_tableau * 2` directement.

import numpy as np

arr = np.arange(1, 6)
print(arr * 2)
print(arr + 10)

