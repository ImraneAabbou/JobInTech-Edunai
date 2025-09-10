# initial = $5000, contribution_mensuelle = $200
# taux_annuel = 7%, temps = 10 ans
# Calculez le montant final avec intérêts composés et contributions mensuelles

initial = 5000
taux_annuel = .07
temps_ans = 10

contribution_mensuelle = 200
taux_mentuel = taux_annuel / 12
temps_mois = temps_ans * 12

montant_final = initial * (1 + taux_mentuel) ** temps_mois
montant_final += contribution_mensuelle * (((1 + taux_mentuel)**temps_mois - 1) / taux_mentuel)

print(f"montant final: {montant_final}")
