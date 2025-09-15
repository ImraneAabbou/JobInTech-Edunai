#     Retirer un Produit Arrêté
#     Utilisez la méthode `.pop()` pour retirer la clé 'est_actif' et stocker sa valeur dans une variable.
#     Affichez la valeur retirée et le dictionnaire mis à jour.
#
# 💡 `valeur_retiree = mon_dict.pop('cle_a_retirer')`.

products = {
    "nom": "",
    "prix": 150,
    "est_actif": False,
}

print("la valeur retirée:", products.pop("est_actif"))
print("le dictionnaire mis à jour:", products)
