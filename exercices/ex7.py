# Un prêt est approuvé si le `score_credit` est > 700 ET le `revenu` est > 50 000€. Affichez 'Approuvé' ou 'Refusé'.
score_credit = 720
revenu = 48000
decision = ""

if score_credit > 700 and revenu > 50000:
    decision = "Approuvé"
else:
    decision = "Refusé"

print(decision)
