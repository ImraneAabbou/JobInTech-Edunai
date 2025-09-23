# Créez une classe `CompteBancaire`.
# Dans `__init__`, stockez le solde comme un attribut 'privé' en utilisant un double souligné: `self.__solde = solde_initial`.
# Créez une méthode `get_solde()` pour retourner le solde.
# Empêchez la modification directe de `__solde` depuis l'extérieur de la classe.
#
# Créez un compte, obtenez le solde, puis essayez de définir `compte.__solde = 1000000` et voyez si `get_solde()` est affecté.
#
# 💡 Le double souligné déclenche le 'name mangling', ce qui le rend plus difficile d'accès direct.

class CompteBancaire:
    def __init__(self, solde_initial):
        self.__solde = solde_initial

    def get_solde(self):
        return self.__solde

compte = CompteBancaire(500)
print(compte.get_solde())
compte.__solde = 1000000
print(compte.get_solde())

