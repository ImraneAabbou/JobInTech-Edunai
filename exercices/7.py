# En utilisant les classes de l'exercice précédent, redéfinissez la méthode `conduire()` dans la classe `Voiture`.
# La nouvelle méthode `conduire()` devrait imprimer 'Conduite d'une voiture sur la route.'
#
# Créez un objet `Voiture` et appelez `conduire()`. Il devrait afficher le nouveau message.
#
# 💡 Définissez simplement une méthode dans la classe enfant avec le même nom que la méthode du parent.


class Vehicule:
    def conduire(self):
        print("Conduite d'un véhicule.")


class Voiture(Vehicule):
    def conduire(self):
        print("Conduite d'une voiture sur la route.")


v = Voiture()
v.conduire()
