#     Créez une classe parent `Vehicule` avec une méthode `conduire()` qui imprime 'Conduite d'un véhicule.'
#     Créez une classe enfant `Voiture` qui hérite de `Vehicule` et a sa propre méthode `klaxonner()` qui imprime 'Klaxon! Klaxon!'.
#
# Créez un objet `Voiture` et appelez ses méthodes `conduire()` et `klaxonner()`.
#
# 💡 Pour hériter, utilisez `class Voiture(Vehicule):`.


class Vehicule:
    def klaxonner(self):
        print("Klaxon! Klaxon!")

    def conduire(self):
        print("Conduite d'un véhicule.")

class Voiture(Vehicule):
    pass


v = Voiture()

v.conduire()
v.klaxonner()
