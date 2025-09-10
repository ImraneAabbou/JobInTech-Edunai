#Calculez l'intérêt total sur un prêt de 20000$ à 6% sur 5 ans
#Ajoutez l'intérêt au principal pour obtenir le montant total dû
#Divisez le total par 60 mois pour trouver le montant du paiement mensuel

principal = 20000
taux = 0.06
annees = 5
mois = annees * 12
interet = principal * taux * annees
interet_mensuel = principal / mois

print(
    f"principal={principal}\n",
    f"interet_mensuel={interet_mensuel}\n",
    sep=""
)
