# 1. Créez une classe `Produit` avec `nom`, `prix`, `id_produit`.
# 2. Créez une classe `Client` avec `nom` et `email`.
# 3. Créez une classe `Commande` qui a un objet `client` et une liste d'objets `produit`.
# 4. La classe `Commande` devrait avoir une méthode pour calculer le coût total de la commande.
#
# 💡 Un objet `Commande` contiendra d'autres objets comme attributs: `self.client = objet_client`.


class Produit:
    def __init__(self, id_produit, nom, prix):
        self.id_produit = id_produit
        self.nom = nom
        self.prix = prix


class Client:
    def __init__(self, nom: str, email: str):
        self.nom = nom
        self.email = email


class Commande:
    def __init__(self, client: Client, produits: list[Produit]):
        self.client = client
        self.produits = produits

    def get_total(self):
        return sum(p.prix for p in self.produits)


c = Client("Alice", "alice@example.com")
p1 = Produit(1, "Livre", 15)
p2 = Produit(2, "Stylo", 5)

commande = Commande(c, [p1, p2])


print(commande.get_total())
