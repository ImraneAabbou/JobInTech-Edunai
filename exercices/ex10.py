# Calculez une taxe de 8.5% sur une facture de restaurant de 45.60$
# Calculez un pourboire de 18% sur le montant original de la facture (avant taxes)
# Additionnez la facture + la taxe + le pourboire pour obtenir le montant final à payer

facture_perc = .085
pourboire_perc = .18
montant_ttl = 45.6


montant_ttl += montant_ttl * facture_perc

montant_ttl += montant_ttl * pourboire_perc

print(f"montant total: {montant_ttl}")
