#     Calculez les frais de port : Si le total d'une commande est supérieur à 50€, la livraison est gratuite. Sinon, elle coûte 5€.
#
# 💡 Vous pouvez utiliser un opérateur ternaire pour une solution concise.

ttl_cmd = 250

livraison_frais = 0 if ttl_cmd > 50 else 5    


print("Total cmd:", ttl_cmd, "; Livraison frais:", livraison_frais)
