# Étape 1 : Vérifiez `score_credit` > 650. Sinon, refuser.
# Étape 2 : Si le crédit est bon, vérifiez `revenu` > 40 000€. Sinon, refuser.
# Étape 3 : Si les deux sont bons, vérifiez `ratio_dette_revenu` < 0.4. Sinon, refuser.
# Si tout est bon, approuver.
score_credit = 700
revenu = 45000
ratio_dette_revenu = 0.35
decision = ""

if score_credit > 650:
    if revenu > 40000:
        if ratio_dette_revenu < 0.4:
            decision = "Approuvé"
        else:
            decision = "Refusé"
    else:
        decision = "Refusé"
else:
    decision = "Refusé"

print(decision)
