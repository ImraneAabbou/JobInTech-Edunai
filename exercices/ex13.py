# Créez des listes pour noms_boissons ['Espresso', 'Latte', 'Cappuccino', 'Americano'], ventes_matin [25, 45, 30, 20], ventes_apres_midi [15, 35, 25, 30], et prix [3.50, 4.75, 4.25, 3.25]
# Calculez les ventes quotidiennes totales en quantité pour chaque boisson
# Calculez les revenus quotidiens totaux pour chaque type de boisson
# Trouvez la boisson la plus populaire (ventes totales les plus élevées)
# Déterminez quelle période (matin vs après-midi) génère plus de revenus


noms_boissons = ['Espresso', 'Latte', 'Cappuccino', 'Americano']
ventes_matin = [25, 45, 30, 20]
ventes_apres_midi = [15, 35, 25, 30]
prix = [3.50, 4.75, 4.25, 3.25]


boissons_ventes_prix_zipped = list(zip(noms_boissons, ventes_matin, ventes_apres_midi, prix))


list(map(lambda b: print(f"{b[0]} -> {(b[1] + b[2] ) * b[3]}"), boissons_ventes_prix_zipped))


boisson_populaire = sorted(boissons_ventes_prix_zipped, key=lambda b: b[1] + b[2], reverse=True)[0]

print("boisson populaire:", boisson_populaire[0])


list(map(lambda b: print(f"{b[0]} -> {'Matin' if (b[1] > b[2]) else 'Apres Midi'}"), boissons_ventes_prix_zipped))
