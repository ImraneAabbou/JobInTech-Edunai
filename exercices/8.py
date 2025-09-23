# Créez une classe parent `Employe` avec `__init__(self, nom)`.
# Créez une classe enfant `Manager` qui hérite de `Employe` et a `__init__(self, nom, departement)`.
# À l'intérieur de l'`__init__` du `Manager`, utilisez `super().__init__(nom)` pour appeler le constructeur du parent.
#
# Créez un objet `Manager` nommé 'Bob' dans le département 'Ventes'.
#
# 💡 `super()` vous permet d'accéder aux méthodes de la classe parent, ce qui évite de réécrire du code.


class Employe:
    def __init__(self, nom):
        self.nom = nom


class Manager(Employe):
    def __init__(self, nom, departement):
        super().__init__(nom)
        self.departement = departement


m = Manager("Bob", "Ventes")
