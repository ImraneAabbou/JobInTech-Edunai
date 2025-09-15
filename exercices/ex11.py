# Évaluez un employé en fonction de `objectif_ventes_atteint` (booléen) et `score_satisfaction_client` (1-5).
objectif_ventes_atteint = True
score_satisfaction_client = 5
evaluation = ""

if objectif_ventes_atteint and score_satisfaction_client == 5:
    evaluation = "Promotion"
elif objectif_ventes_atteint and score_satisfaction_client > 4:
    evaluation = "Bonus"
elif not objectif_ventes_atteint or score_satisfaction_client < 3:
    evaluation = "Doit s'améliorer"
else:
    evaluation = "Aucune distinction"

print(evaluation)
