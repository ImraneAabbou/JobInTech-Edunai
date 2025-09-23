# 1. Créez une classe `Livre` avec `titre`, `auteur`, `isbn`.
# 2. Créez une classe `Bibliotheque` qui contient une liste d'objets `Livre`.
# 3. La classe `Bibliotheque` devrait avoir des méthodes pour `ajouter_livre(livre)`, `trouver_livre_par_titre(titre)`, et `lister_tous_les_livres()`.
#
# 💡 La classe `Bibliotheque` gère une collection d'objets `Livre`. C'est un modèle de POO courant et puissant.

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def trouver_livre_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                return livre
        return None

    def lister_tous_les_livres(self):
        return [(livre.titre, livre.auteur, livre.isbn) for livre in self.livres]

b = Bibliotheque()
l1 = Livre("1984", "George Orwell", "12345")
l2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "67890")

b.ajouter_livre(l1)
b.ajouter_livre(l2)

print(b.lister_tous_les_livres())

