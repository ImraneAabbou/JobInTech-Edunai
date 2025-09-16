# 1. On vous donne une liste de dictionnaires de produits.
# 2. Initialisez `revenu_total` à 0.
# 3. Parcourez la liste `produits`. Pour chaque produit, calculez sa valeur totale (`prix` * `quantite`).
# 4. Ajoutez cette valeur au `revenu_total`.
# 5. Affichez le `revenu_total` final.
# Données : `produits = [{'nom': 'Ordinateur', 'prix': 1200, 'quantite': 5}, {'nom': 'Souris', 'prix': 25, 'quantite': 30}]`
# 💡 À l'intérieur de la boucle, vous accéderez aux valeurs du dictionnaire comme `produit['prix']`.

produits = [
    {'nom': 'Ordinateur', 'prix': 1200, 'quantite': 5},
    {'nom': 'Souris', 'prix': 25, 'quantite': 30}
]

revenu_total = 0

for produit in produits:
    revenu_total += produit['prix'] * produit['quantite']

print(revenu_total)

