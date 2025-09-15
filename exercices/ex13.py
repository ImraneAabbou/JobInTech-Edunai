# La prime de base est de 500€. Si l'`âge` est inférieur à 25 ans, ajoutez 200€. Si `a_eu_accidents` est `True`, ajoutez 300€.
# Si l'`âge` est supérieur à 60 ANS ET `a_eu_accidents` est `False`, accordez une réduction de 100€.
age = 62
a_eu_accidents = False

prime = 500

if age < 25:
    prime += 200

if a_eu_accidents:
    prime += 300

if age > 60 and not a_eu_accidents:
    prime -= 100

print(prime)
