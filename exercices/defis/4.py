# Créez une fonction `generer_rapport_notes(nom_etudiant, notes)` où `notes` est une liste de nombres.
# La fonction doit :
# 1. Calculer la note moyenne de l'étudiant.
# 2. Déterminer si l'étudiant a réussi (moyenne > 60) ou échoué.
# 3. Retourner une chaîne de rapport formatée : `Rapport de Notes pour [Nom Étudiant]\nMoyenne : [Moyenne (2 décimales)]\nStatut : [Réussi/Échoué]`.
#
# Générez un rapport pour 'Sophie Martin' avec les notes `[75, 88, 62, 91, 55]`.
#
# 💡 Utilisez `sum()` et `len()` pour la moyenne. Les f-strings pour le formatage. Les conditions pour le statut.


def generer_rapport_notes(nom_etudiant, notes):
    moyenne = sum(notes) / len(notes)
    statut = "Réussi" if moyenne > 60 else "Échoué"
    return f"Rapport de Notes pour {nom_etudiant}\nMoyenne : {moyenne:.2f}\nStatut : {statut}"


notes_etudiante = [75, 88, 62, 91, 55]
print(generer_rapport_notes("Someone", notes_etudiante))
