# 1. Définir la fonction obtenir_prix_final(prix_base, taux_taxe=0.08).
# 2. Calculer le prix final = prix_base * (1 + taux_taxe).
# 3. Retourner le résultat.
# 4. Tester avec prix_base=50 (taxe par défaut) et prix_base=100 avec taux_taxe=0.10.

def obtenir_prix_final(prix_base, taux_taxe=0.08):
    return prix_base * (1 + taux_taxe)

# Tests
prix1 = obtenir_prix_final(50)         # taxe par défaut (8%)
prix2 = obtenir_prix_final(100, 0.10)  # taxe personnalisée (10%)

print(prix1)
print(prix2)

