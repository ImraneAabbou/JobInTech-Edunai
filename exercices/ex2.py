# Créez une variable `prix_total` avec la valeur 75.50
# Créez une variable `est_membre_premium` avec la valeur `True`
# Vérifiez si le `prix_total` est supérieur à 100 OU si le client `est_membre_premium` pour appliquer la réduction

prix_total = 75.50
est_membre_premium = True
can_have_reduction = (prix_total > 100) or (est_membre_premium)

print("reduction: ", can_have_reduction)
