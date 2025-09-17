# 1. Définir la fonction est_adulte(age).
# 2. Vérifier si age >= 18.
# 3. Retourner True si c’est le cas, sinon False.
# 4. Tester avec age = 20 et age = 16.
# 5. Afficher les résultats.

def est_adulte(age):
    if age >= 18:
        return True
    else:
        return False

print(est_adulte(20))  # Doit afficher True
print(est_adulte(16))  # Doit afficher False

