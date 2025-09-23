# 1. Créez une classe de base `Vehicule` avec `marque`, `modele`, et un booléen `est_loue`.
# 2. Créez des classes enfants `Voiture` et `Moto` qui héritent de `Vehicule`.
# 3. Créez une classe `AgenceDeLocation` qui gère une flotte d'objets `Vehicule`.
# 4. L' `AgenceDeLocation` devrait avoir des méthodes pour `louer_vehicule(modele)` et `retourner_vehicule(modele)` qui changent le statut `est_loue`.
#
# 💡 L'`AgenceDeLocation` devra parcourir sa liste de véhicules pour trouver le bon à louer ou à retourner.


class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.est_loue = False


class Voiture(Vehicule):
    pass


class Moto(Vehicule):
    pass


class AgenceDeLocation:
    def __init__(self):
        self.vehicules = []

    def ajouter_vehicule(self, vehicule):
        self.vehicules.append(vehicule)

    def louer_vehicule(self, modele):
        for v in self.vehicules:
            if v.modele == modele and not v.est_loue:
                v.est_loue = True
                return f"{modele} a été loué."
        return f"{modele} non disponible."

    def retourner_vehicule(self, modele):
        for v in self.vehicules:
            if v.modele == modele and v.est_loue:
                v.est_loue = False
                return f"{modele} a été retourné."
        return f"{modele} n'était pas loué."


a = AgenceDeLocation()
v1 = Voiture("Toyota", "Corolla")
v2 = Moto("Yamaha", "MT-07")

a.ajouter_vehicule(v1)
a.ajouter_vehicule(v2)

print(a.louer_vehicule("Corolla"))
print(a.louer_vehicule("Corolla"))
print(a.retourner_vehicule("Corolla"))
print(a.retourner_vehicule("Corolla"))
