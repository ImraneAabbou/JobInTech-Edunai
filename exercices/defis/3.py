# 1. Simulez un système d'inventaire qui s'arrête lorsque le stock est bas.
# 2. Démarrez une boucle `while` qui continue tant que `niveau_stock` est supérieur au `seuil_recommande`.
# 3. À l'intérieur de la boucle, simulez une vente en soustrayant un nombre aléatoire (par ex., entre 1 et 5) du `niveau_stock`.
# 4. Affichez le nouveau niveau de stock à chaque itération.
# 5. Après la fin de la boucle, affichez un message comme `Le stock est bas (12 unités) ! Il est temps de réapprovisionner.`
# Données : `import random`, `niveau_stock = 50`, `seuil_recommande = 15`
# 💡 Vous aurez besoin de `import random` en haut de votre script. Utilisez `random.randint(1, 5)` pour obtenir un montant de vente aléatoire.

import random

niveau_stock = 50
seuil_recommande = 15

while niveau_stock > seuil_recommande:
    vente = random.randint(1, 5)
    niveau_stock -= vente
    print(f"Niveau de stock actuel : {niveau_stock}  --  {vente} vente(s)")

print(f"Le stock est bas ({niveau_stock} unités) ! Il est temps de réapprovisionner.")
