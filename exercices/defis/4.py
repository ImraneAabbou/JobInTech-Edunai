# 1. Vous avez une liste de résultats de sondage, dont certains sont invalides (marqués par `-1`).
# 2. Créez une liste vide `resultats_valides` et une variable `score_total_valide = 0`.
# 3. Parcourez `resultats_sondage`. Utilisez `continue` pour sauter les résultats invalides.
# 4. Pour les résultats valides, ajoutez-les à `score_total_valide` et ajoutez-les également à la liste `resultats_valides`.
# 5. Après la boucle, calculez et affichez la moyenne des scores valides.
# Données : `resultats_sondage = [8, 9, -1, 10, 7, -1, 9]`
# 💡 La moyenne est `score_total_valide / len(resultats_valides)`. Faites attention de ne pas diviser par zéro s'il n'y a aucun résultat valide !

resultats_sondage = [8, 9, -1, 10, 7, -1, 9]

resultats_valides = []
score_total_valide = 0

for score in resultats_sondage:
    if score == -1:
        continue
    resultats_valides.append(score)
    score_total_valide += score

if resultats_valides:
    moyenne = score_total_valide / len(resultats_valides)
    print(f"Moyenne des scores valides : {moyenne:.2f}")
else:
    print("Aucun score valide disponible.")


