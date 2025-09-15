#     Créez un dictionnaire `menu` avec des plats comme clés et des prix comme valeurs (ex: 'Pizza': 12.50).
#     Utilisez la méthode `.get()` pour vérifier en toute sécurité le prix du 'Sushi', en fournissant un message par défaut s'il n'est pas trouvé.
#     Affichez le résultat.
#
# 💡 `menu.get('Sushi', 'Plat non disponible')` prévient les erreurs.

menu = {
    "pizza": 12.5,
}

print("Sushi:", menu.get("Sushi", "n'est pas trouvé"))
