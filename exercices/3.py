#     Créez une classe `CompteBancaire` avec `nom_titulaire` et `solde`.
#     Ajoutez une méthode `deposer(montant)` qui ajoute au solde.
#     Ajoutez une méthode `retirer(montant)` qui soustrait du solde mais vérifie d'abord les fonds suffisants.
#
# Créez un compte, déposez 100, puis essayez de retirer 50, et ensuite essayez de retirer 200.
#
# 💡 La méthode retirer aura besoin d'une instruction `if`: `if montant <= self.solde:`.


class CompteBancaire:
    def __init__(self, solde_initial: int):
        self.solde = solde_initial

    def deposer(self, montant: int):
        self.solde += montant

    def retirer(self, montant: int):
        if not (montant <= self.solde):
            return

        self.solde -= montant


c = CompteBancaire(0)
c.deposer(100)
print("solde apres c.deposer(100):", c.solde)
c.retirer(50)
print("solde apres c.retirer(50):", c.solde)
c.retirer(200)
print("solde apres c.retirer(200):", c.solde)


