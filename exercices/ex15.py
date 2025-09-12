#    Définissez `poids_colis_kg` = 2.5, `pays_destination` = 'FR', `envoi_express` = `True`
#    Calculez le coût de base (poids * 5€). Calculez le supplément international (10€ si le pays n'est pas 'FR')
#    Calculez les frais express (15€ si `envoi_express` est `True`). Affichez le coût total.
#
#💡 Vous aurez besoin de plusieurs variables pour suivre les coûts. La comparaison de chaînes est `pays_destination == 'FR'`


poids_colis_kg = 2.5
pays_destination = 'FR'
envoi_express = True


cout_de_base = poids_colis_kg * 5
sup_international = 10 * (pays_destination != 'FR')
frais_express = 15 * envoi_express

total = cout_de_base + sup_international + frais_express

print("Total:", total)
