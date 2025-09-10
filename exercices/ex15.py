# facture = $156.75, taxe = 8.25%, pourboire = 20%, personnes = 6
# paiements_extra = [personne1: +$10, personne2: +$5]
# Calculez les montants individuels avec divisions personnalisées

facture = 156.75
taxe = .0825
pourboire = .2
personnes = 6

montant_p1 = 10
montant_p2 = 5

montant_total = facture * (1 + taxe)
montant_total += montant_total * pourboire

montant_individuel = (montant_total - montant_p1 - montant_p2) / 6

print(
    f"montant individuel pour personne 1: {montant_individuel + montant_p1}", "\n",
    f"montant individuel pour personne 2: {montant_individuel + montant_p2}", "\n",
    f"montant individuel pour les autres: {montant_individuel}", "\n",
    sep=""
)
