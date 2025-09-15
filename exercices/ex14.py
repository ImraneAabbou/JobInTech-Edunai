# Un utilisateur bénéficie de la livraison gratuite si : (`total_panier` > 100€ ET `est_membre_premium`) OU il a un `coupon_livraison_gratuite`.
# Un utilisateur obtient une réduction de 10% si : il est un `membre_premium` OU (`total_panier` > 200€ ET NON `a_autres_reductions`).
total_panier = 220
est_membre_premium = False
coupon_livraison_gratuite = True
a_autres_reductions = False

avantages = []

if (total_panier > 100 and est_membre_premium) or coupon_livraison_gratuite:
    avantages.append("Livraison gratuite")

if est_membre_premium or (total_panier > 200 and not a_autres_reductions):
    avantages.append("Réduction de 10%")

print(avantages)
