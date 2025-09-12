# Définissez `total_panier` = 120.00, `est_client_fidele` = `True`, `code_promo` = 'ETE20'
# Créez une variable `livraison_gratuite` si le total est > 100 OU si le client est fidèle
# Créez une variable `reduction_supplementaire` si `livraison_gratuite` est vraie ET si le `code_promo` est 'ETE20'
# 💡 Combinez les opérateurs `or` et `and` dans la bonne séquence


total_panier = 120.00
est_client_fidele = True
code_promo = 'ETE20'

livraison_gratuite = (total_panier > 100) or est_client_fidele
reduction_supplementaire = (code_promo == "ETE20") and livraison_gratuite


print("livraison_gratuite:", livraison_gratuite, "; reduction_supplementaire:", reduction_supplementaire)
