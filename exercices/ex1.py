# 1. Utilisez une boucle `for` pour calculer le `total_ventes` à partir de la liste `ventes_quotidiennes`.
# 2. Calculez le montant de la `vente_moyenne` (total des ventes / nombre de ventes).
# 3. Affichez le total et la moyenne des ventes, formatés avec deux décimales.
ventes_quotidiennes = [150.50, 88.00, 230.25, 50.75, 190.00]

total_ventes = 0
for vente in ventes_quotidiennes:
    total_ventes += vente

vente_moyenne = total_ventes / len(ventes_quotidiennes)

print(f"Total des ventes : {total_ventes:.2f} €")
print(f"Vente moyenne : {vente_moyenne:.2f} €")
