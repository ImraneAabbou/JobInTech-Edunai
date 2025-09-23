# Créez une classe `Panier`.
# Dans son `__init__`, créez une liste vide `self.articles`.
# Créez une méthode `ajouter_article(produit)` qui ajoute un objet produit à la liste.
# Créez une méthode `get_total()` qui calcule le prix total de tous les produits dans le panier.
#
# Créez d'abord une classe `Produit`. Ensuite, créez un `Panier`, ajoutez-y plusieurs objets `Produit`, et obtenez le total.
#
# 💡 Ceci démontre la composition, où un objet contient d'autres objets.


class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Panier:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, produit):
        self.articles.append(produit)

    def get_total(self):
        return sum(p.prix for p in self.articles)


p1 = Produit("Pomme", 2)
p2 = Produit("Banane", 3)
p3 = Produit("Orange", 4)

panier = Panier()
panier.ajouter_article(p1)
panier.ajouter_article(p2)
panier.ajouter_article(p3)

print(panier.get_total())
