#    Définissez `revenu_annuel` = 55000, `score_credit` = 720, `duree_emploi_annees` = 3
#    Créez des variables booléennes pour chaque condition : `revenu_suffisant` (>50k), `score_credit_bon` (>700), `emploi_stable` (>2 ans)
#    Combinez les trois booléens pour décider si le prêt est `approuve` (tous doivent être vrais)
#
#💡 Utilisez l'opérateur `and` pour combiner les conditions finales

revenu_annuel = 55000
score_credit = 720
duree_emploi_annees = 3

min_revenu_suffisant = 50000
min_score_credit_bon = 700
min_emploi_annees = 2 # stabilite

est_approuve = (revenu_annuel > min_revenu_suffisant) and (score_credit > min_score_credit_bon) and (min_emploi_annees > min_emploi_annees)

print("credit approuve:", est_approuve)
