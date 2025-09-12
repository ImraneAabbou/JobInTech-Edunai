# Créez une variable `prix_chaine` avec la valeur '199.99'
# Convertissez cette chaîne en un nombre décimal (float) en utilisant `float()`
# Affichez le type de la nouvelle variable de prix pour confirmer que c'est bien un float

prix_chaine = '199.99'
prix_float = float(prix_chaine)
# is_float = isinstance(prix_float, float)
is_float = type(prix_float) is float

print("c'est un float: ", is_float)
