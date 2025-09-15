#     Créez un dictionnaire où les clés sont des noms de villes ('Paris', 'Londres').
#     La valeur pour chaque ville doit être un autre dictionnaire représentant son inventaire (ex: {'ordinateurs': 10, 'souris': 50}).
#     Écrivez du code pour afficher le stock d''ordinateurs' à 'Londres'.
#
# 💡 Accédez aux données imbriquées avec plusieurs clés : `inventaire['Londres']['ordinateurs']`.


inventaire = {
    "Paris": {"ordinateurs": 200, "souris": 250},
    "Londres": {"ordinateurs": 120, "souris": 500},
}


print("[*] Paris:")
print("\t", "ordinateurs:", inventaire["Paris"]["ordinateurs"])
print("\t", "souris:", inventaire["Paris"]["ordinateurs"])

print("[*] Londres:")
print("\t", "ordinateurs:", inventaire["Londres"]["ordinateurs"])
print("\t", "souris:", inventaire["Londres"]["ordinateurs"])
