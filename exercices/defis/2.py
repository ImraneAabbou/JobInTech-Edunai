# 1. Créez une classe de base `Employe` avec `nom`, `id_employe`, et une méthode `calculer_paie()`.
# 2. Créez deux classes enfants, `EmployeSalarie` et `EmployeHoraire`, qui héritent de `Employe`.
# 3. Redéfinissez `calculer_paie()` dans chaque classe enfant pour implémenter une logique différente (ex: salaire fixe vs. heures_travaillees * taux_horaire).
#
# 💡 Ceci montre le polymorphisme: vous pouvez appeler `.calculer_paie()` sur n'importe quel objet employé, et il fera la bonne chose en fonction de sa classe.

class Employe:
    def __init__(self, nom, id_employe):
        self.nom = nom
        self.id_employe = id_employe

    def calculer_paie(self):
        pass

class EmployeSalarie(Employe):
    def __init__(self, nom, id_employe, salaire):
        super().__init__(nom, id_employe)
        self.salaire = salaire

    def calculer_paie(self):
        return self.salaire

class EmployeHoraire(Employe):
    def __init__(self, nom, id_employe, heures_travaillees, taux_horaire):
        super().__init__(nom, id_employe)
        self.heures_travaillees = heures_travaillees
        self.taux_horaire = taux_horaire

    def calculer_paie(self):
        return self.heures_travaillees * self.taux_horaire

e1 = EmployeSalarie("Bob", 1, 3000)
e2 = EmployeHoraire("Alice", 2, 160, 20)

print(e1.calculer_paie())
print(e2.calculer_paie())

