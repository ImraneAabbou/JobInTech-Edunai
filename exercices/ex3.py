# 1. Parcourez le dictionnaire `inventaire` en utilisant `.items()` pour accéder à la fois au nom du produit et à son stock.
# 2. Pour chaque produit, affichez une chaîne formatée comme : `Produit : Ordinateur, Stock : 12`.
# 3. Dans la même boucle, vérifiez si le stock est inférieur à 10. Si c'est le cas, affichez un avertissement : `Alerte : Stock faible pour Clavier !`.
inventaire = {'Ordinateur': 12, 'Souris': 45, 'Clavier': 8, 'Écran': 21}

for produit, stock in inventaire.items():
    print(f"Produit : {produit}, Stock : {stock}")
    if stock < 10:
        print(f"Alerte : Stock faible pour {produit} !")

