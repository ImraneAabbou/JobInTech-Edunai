#     Créez une classe `Employe` avec les attributs `nom` et `role`.
#     Ajoutez une méthode `afficher_infos()` qui imprime une chaîne comme 'Nom: Jean Dupont, Rôle: Développeur'.
#
# Créez un objet Employe et appelez sa méthode `afficher_infos()`.
#
# 💡 Une méthode est une fonction à l'intérieur d'une classe. N'oubliez pas `self`: `def afficher_infos(self): ...`


class Employe:
    def __init__(self, nom, role):
        self.nom = nom
        self.role = role

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Rôle: {self.role}")

e = Employe("Someone", "Something")
e.afficher_infos()
