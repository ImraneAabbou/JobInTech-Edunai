# Créez une classe nommée `Produit`.
# Donnez-lui trois attributs dans la méthode `__init__`: `nom`, `prix` et `stock`.
#
# Instanciez (créez) un objet pour un 'Ordinateur' qui coûte 1200 et a un stock de 15.
#
# 💡 Rappelez-vous du mot-clé `self`: `def __init__(self, nom, prix, stock): self.nom = nom ...`


class Produit:
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock


ordinateur = Produit("HP", 2100, 150)


