#     Créez un dictionnaire de produits où chaque clé est un ID de produit (ex: 'P001').
#     La valeur pour chaque produit doit être un autre dictionnaire avec les clés 'nom', 'prix', et 'stock'.
#     Écrivez du code pour ajouter un nouveau produit.
#     Écrivez du code pour mettre à jour le stock d'un produit existant.
#
# 💡 C'est un dictionnaire imbriqué. Accédez aux données comme `produits['P001']['prix']`.


produits = {
    "P001": {
        "nom": "Something",
        "prix": 20,
        "stock": 100,
    },
}


nouv_prod = {
    "nom": "Something cool",
    "prix": 25,
    "stock": 90,
}

produits["P002"] = nouv_prod

print(produits)
