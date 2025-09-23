# 1. Créez une classe `CompteBancaire` avec encapsulation pour le solde (`__solde`).
# 2. Créez des classes enfants `CompteEpargne` (qui ajoute un taux d'intérêt) et `CompteCourant` (qui pourrait avoir une limite de découvert).
# 3. Redéfinissez la méthode `retirer` dans `CompteCourant` pour autoriser les découverts jusqu'à la limite.
# 4. Créez une classe `Transaction` pour enregistrer chaque dépôt et retrait pour un compte.
#
# 💡 L'objet `CompteBancaire` peut avoir une liste d'objets `Transaction` pour conserver un historique. Cela combine tous les concepts clés de la POO.


class Transaction:
    def __init__(self, type_op, montant):
        self.type_op = type_op
        self.montant = montant


class CompteBancaire:
    def __init__(self, solde_initial):
        self.__solde = solde_initial
        self.transactions = []

    def get_solde(self):
        return self.__solde

    def deposer(self, montant):
        self.__solde += montant
        self.transactions.append(Transaction("depot", montant))

    def retirer(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
            self.transactions.append(Transaction("retrait", montant))
        else:
            print("Solde insuffisant")


class CompteEpargne(CompteBancaire):
    def __init__(self, solde_initial, taux_interet):
        super().__init__(solde_initial)
        self.taux_interet = taux_interet

    def appliquer_interet(self):
        interet = self.get_solde() * self.taux_interet
        self.deposer(interet)


class CompteCourant(CompteBancaire):
    def __init__(self, solde_initial, limite_decouvert):
        super().__init__(solde_initial)
        self.limite_decouvert = limite_decouvert

    def retirer(self, montant):
        if montant <= self.get_solde() + self.limite_decouvert:
            self._CompteBancaire__solde -= montant
            self.transactions.append(Transaction("retrait", montant))
        else:
            print("Dépasse la limite de découvert")


compte = CompteCourant(200, 50)

compte.retirer(150)
print(compte.get_solde())

compte.retirer(80)
print(compte.get_solde())

compte.retirer(20)
print(compte.get_solde())

compte.retirer(10)
print(compte.get_solde())

compte.deposer(100)
print(compte.get_solde())

print("-" * 25)

compte_epargne = CompteEpargne(1000, 0.05)

compte_epargne.deposer(200)
print(compte_epargne.get_solde())

compte_epargne.retirer(100)
print(compte_epargne.get_solde())

compte_epargne.appliquer_interet()
print(compte_epargne.get_solde())
