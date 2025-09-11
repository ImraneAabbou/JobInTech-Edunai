# Créez une variable de prix avec la valeur `59.9`
# Utilisez une f-string pour formater ce nombre en une chaîne avec deux décimales et un symbole monétaire
# Affichez la chaîne formatée : 'Prix : 59,90 €'

# 💡 La mise en forme de f-string : .2f est ce dont vous avez besoin. N'oubliez pas le symbole €

price = 59.9
formatted_price = f"{price:,.2f} €"

print(f"Prix : {formatted_price}")
