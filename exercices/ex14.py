# Créez des listes pour noms_membres ['John', 'Sarah', 'Mike', 'Lisa', 'Tom'], visites_mensuelles [12, 18, 8, 22, 15], mois_adhesion [6, 12, 3, 18, 9], et frais_mensuels [50, 75, 40, 100, 60]
# Calculez les revenus totaux générés par chaque membre (mois × frais mensuels)
# Trouvez les membres avec une fréquence de visite supérieure à la moyenne
# Calculez la moyenne des visites par mois pour tous les membres
# Identifiez le membre le plus précieux (revenus totaux les plus élevés) et le membre le plus actif (visites les plus élevées)

noms_membres = ["John", "Sarah", "Mike", "Lisa", "Tom"]
visites_mensuelles = [12, 18, 8, 22, 15]
mois_adhesion = [6, 12, 3, 18, 9]
frais_mensuels = [50, 75, 40, 100, 60]

info_zipped = list(zip(noms_membres, visites_mensuelles, mois_adhesion, frais_mensuels))
moyenne_visites = sum(visites_mensuelles) / len(visites_mensuelles)

for i in info_zipped:
    print(
        f"{i[0]} --> {i[2] * i[3]}",
        (i[1] > moyenne_visites)
        * f"(visites mensuelle '{i[1]}' inferieur a la moyenne)",
    )


print("visites les plus élevées:", max(info_zipped, key=lambda i: i[1]))
print("revenus totaux les plus élevés:", max(info_zipped, key=lambda i: i[2] * i[3]))
