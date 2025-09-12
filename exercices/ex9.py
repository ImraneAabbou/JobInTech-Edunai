#    Imaginez trois prix : `prix1` = 49.99, `prix2` = 59.99, `prix3` = 39.99
#    Utilisez `min()` pour trouver le prix le plus bas parmi les trois
#    Utilisez `max()` pour trouver le prix le plus élevé et affichez les deux résultats
#
#💡 `min()` et `max()` peuvent prendre plusieurs arguments : `min(prix1, prix2, prix3)`

prix1 = 49.99
prix2 = 59.99
prix3 = 39.99

prix_min = min(prix1, prix2, prix3)
prix_max = max(prix1, prix2, prix3)

print("min prix:", prix_min, "; max prix:", prix_max)
