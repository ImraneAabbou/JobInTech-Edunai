#     Créez un dictionnaire où les clés sont des noms d'utilisateurs.
#     La valeur pour chaque utilisateur est un tuple de ses catégories de produits préférées (ex: ('Électronique', 'Livres')).
#     Étant donné deux utilisateurs, trouvez s'ils ont des catégories préférées en commun.
#
# 💡 Convertissez les tuples en sets pour trouver facilement l'`intersection`.

users = {
    "someone1": {"Électronique", "Livres"},
    "someone2": {"Food", "Accessoires"},
    "someone3": {"Electro Menage", "Food"},
    "someone4": {"Électronique", "Accessoires"},
}

for username, categories in users.items():
    for u, c in filter(lambda i: i[0] != username, users.items()):
        if categories_commun := categories.intersection(c):
            print(
                f'catégories préférées en commun entre "{username}" et "{u}"',
                categories_commun,
            )
