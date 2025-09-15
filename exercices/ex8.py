#     Créez un dictionnaire `inventaire` : {'pommes': 50, 'oranges': 35}.
#     Créez un autre dictionnaire pour une nouvelle livraison : `nouveau_stock = {'pommes': 25, 'bananes': 40}`.
#     Utilisez la méthode `.update()` pour ajouter le nouveau stock à l'inventaire principal.
#
# 💡 `inventaire.update(nouveau_stock)` fusionne les dictionnaires.

inventaire = {'pommes': 50, 'oranges': 35}

nouveau_stock = {'pommes': 25, 'oranges': 40}

inventaire.update(nouveau_stock)

print(inventaire)

