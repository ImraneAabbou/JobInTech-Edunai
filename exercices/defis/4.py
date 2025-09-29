# 1. Créez deux tableaux NumPy, `heures_etude` et `notes_examen`, avec 10 nombres aléatoires chacun.
# 2. Créez un nuage de points pour visualiser la relation entre les heures d'étude et les notes d'examen.
# 3. Ajoutez un titre 'Heures d'étude vs. Notes d'examen' et des étiquettes d'axes appropriées.
#
# 💡 Utilisez `np.random.rand(10)` pour créer des tableaux aléatoires. Utilisez `plt.scatter(x, y)` pour le graphique.

import numpy as np
import matplotlib.pyplot as plt

heures_etude = np.random.rand(10) * 10
notes_examen = np.random.rand(10) * 100

plt.scatter(heures_etude, notes_examen)
plt.title("Heures d'étude vs. Notes d'examen")
plt.xlabel("Heures d'étude")
plt.ylabel("Notes d'examen")
plt.show()

