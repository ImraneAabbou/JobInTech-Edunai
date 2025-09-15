#     Commencez avec une liste de dictionnaires, où chaque dictionnaire représente une transaction de vente avec les clés 'produit', 'region', et 'montant'.
#     Calculez les ventes totales par région.
#     Calculez les ventes totales par produit.
#     Identifiez le produit le plus vendu.
#
# 💡 Vous devrez parcourir la liste de dictionnaires et utiliser un autre dictionnaire pour stocker les totaux de ventes agrégés.

transactions = [
    {
        "produit": "Wifi ADSL TP-link",
        "region": "Casa Settat",
        "montant": 150,
    },
    {
        "produit": "Wifi ADSL TP-link",
        "region": "Casa Settat",
        "montant": 200,
    },
    {
        "produit": "Smartphone Samsung A14",
        "region": "Rabat Salé Kenitra",
        "montant": 2200,
    },
    {
        "produit": "Laptop Lenovo IdeaPad",
        "region": "Casa Settat",
        "montant": 5400,
    },
    {
        "produit": "Imprimante HP DeskJet",
        "region": "Fès Meknès",
        "montant": 1200,
    },
    {
        "produit": "Laptop Lenovo IdeaPad",
        "region": "Marrakech Safi",
        "montant": 5600,
    },
    {
        "produit": "Smartphone Samsung A14",
        "region": "Casa Settat",
        "montant": 2150,
    },
    {
        "produit": "Tablette iPad Mini",
        "region": "Tanger Tétouan Al Hoceima",
        "montant": 4600,
    },
    {
        "produit": "Imprimante HP DeskJet",
        "region": "Rabat Salé Kenitra",
        "montant": 1150,
    },
    {
        "produit": "Wifi ADSL TP-link",
        "region": "Marrakech Safi",
        "montant": 170,
    },
]


for region in set(map(lambda t: t["region"], transactions)):

    region_montant_sum = sum(
        map(
            lambda t: t["montant"],
            filter(lambda t: t["region"] == region, transactions),
        )
    )

    print(region, ":", region_montant_sum)

print("_" * 5)

for produit in set(map(lambda t: t["produit"], transactions)):

    produit_montant_sum = sum(
        map(
            lambda t: t["montant"],
            filter(lambda t: t["produit"] == produit, transactions),
        )
    )

    print(produit, ":", produit_montant_sum)


print("_" * 5)

produits = list(map(lambda p: p["produit"], transactions))

print("produit plus vendu:", max(set(produits), key=lambda t: produits.count(t)))
