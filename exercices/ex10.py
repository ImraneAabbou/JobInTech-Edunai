#     Créez un dictionnaire `menu` avec au moins trois plats et leurs prix.
#     Utilisez la méthode `.items()` pour obtenir toutes les paires clé-valeur.
#     Affichez la liste des plats.
#
# 💡 `.items()` retourne un objet de vue qui affiche une liste des paires clé-valeur (en tuples) d'un dictionnaire.

menu = {
    "pizza": 20,
    "sandwich": 20,
    "chawarma": 20,
}

menu.items()

for plat, prix in menu.items():
    print(f"{plat}: {prix}")
