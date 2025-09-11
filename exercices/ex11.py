# Définissez des variables pour le nom du client, le nom du produit, la quantité et le prix unitaire
# Calculez le sous-total, une taxe de 8 % et le total final
# Créez un reçu multi-lignes bien formaté en utilisant des f-strings et des caractères spéciaux
# Assurez-vous que les nombres sont formatés à deux décimales

# 💡 Utilisez \t pour l'alignement et :.2f pour le formatage des prix

client_name = "Someone"
product_name = "Something"
product_qty = 4
unit_price = 4444
taxe = .08

# sous-total
total = unit_price * product_qty
total += total * .08

print(f"Prix: {total:.2f}")
