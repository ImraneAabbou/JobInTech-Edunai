# Un client commande un `plat`. Si le `plat` est 'Pizza', vérifiez s'il veut du `fromage_extra`. Affichez la commande finale.
plat = "Pizza"
fromage_extra = True
commande = ""

if plat == "Pizza":
    if fromage_extra:
        commande = "Pizza avec fromage extra"
    else:
        commande = "Pizza"
else:
    commande = plat

print(commande)
