# Décidez de lancer ou non un nouveau produit.
# Lancement si (`score_etude_marche` > 8 ET `marge_beneficiaire_estimee` > 0.2) OU (`concurrent_est_faible` est `True` ET `ressources_internes_disponibles` est `True`).
score_etude_marche = 9
marge_beneficiaire_estimee = 0.25
concurrent_est_faible = False
ressources_internes_disponibles = True
decision = ""

if (score_etude_marche > 8 and marge_beneficiaire_estimee > 0.2) or (concurrent_est_faible and ressources_internes_disponibles):
    decision = "Lancement Recommandé"
else:
    decision = "En attente pour examen plus approfondi"

print(decision)
