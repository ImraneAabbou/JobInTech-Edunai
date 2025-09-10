# Fonctions mathématiques intégrées

print(abs(-15))  # 15 (distance par rapport à zéro)
print(abs(15))   # 15 (déjà positif)

print(round(3.7))    # 4 (arrondit au nombre entier le plus proche)
print(round(3.14159, 2))  # 3.14 (arrondit à 2 décimales)

print(min(5, 3, 8, 1))  # 1 (plus petite valeur)
print(max(5, 3, 8, 1))  # 8 (plus grande valeur)

print(pow(2, 3))  # 8 (2 puissance 3)
print(pow(5, 2))  # 25 (5 puissance 2)


# Calculs simples utilisant les fonctions mathématiques

# Calculer le pourboire sur une facture de 47,83$ (pourboire de 18,5%)
print("Montant de la facture:", 47.83)
print("Montant du pourboire:", round(47.83 * 0.185, 2))
print("Total avec pourboire:", round(47.83 + (47.83 * 0.185), 2))

# Trouver la meilleure offre parmi les prix
print("Prix le moins cher:", min(12.99, 15.50, 9.75, 18.25))
print("Le plus cher:", max(12.99, 15.50, 9.75, 18.25))


# Ordre des opérations

# Sans parenthèses - suit l'ordre des opérations
print(2 + 3 * 4)      # 14 (pas 20 !)
print(10 - 6 / 2)     # 7.0 (pas 2.0 !)
print(2 ** 3 * 4)     # 32 (pas 4096 !)

# Avec parenthèses - force l'ordre désiré
print((2 + 3) * 4)    # 20
print((10 - 6) / 2)   # 2.0
print(2 ** (3 * 4))   # 4096

# Exemples de nombres binaires

# Convertir des nombres en binaire
print(bin(5))    # 0b101 (5 en binaire)
print(bin(10))   # 0b1010 (10 en binaire)
print(bin(255))  # 0b11111111 (255 en binaire)

# Convertir le binaire vers décimal
print(int('101', 2))    # 5
print(int('1010', 2))   # 10
print(int('11111111', 2))  # 255


# Travail avec des nombres complexes

# Créer et travailler avec des nombres complexes directement
print("Nombre complexe:", 3 + 4j)
print("Autre complexe:", 1 + 2j)

# Opérations de base avec les nombres complexes
print("Addition:", (3 + 4j) + (1 + 2j))
print("Multiplication:", (3 + 4j) * (1 + 2j))

# Obtenir les parties réelle et imaginaire
print("Partie réelle:", (3 + 4j).real)
print("Partie imaginaire:", (3 + 4j).imag)


# Conversion entre les systèmes

# Décimal vers autres bases
print("Décimal: 42")
print("Binaire:", bin(42))
print("Octal:", oct(42))
print("Hexadécimal:", hex(42))

# Reconvertir vers décimal
print("Du binaire:", int('101010', 2))
print("De l'octal:", int('52', 8))
print("De l'hexadécimal:", int('2a', 16))


# Variables pour un système de gestion d'inventaire
nom_produit = "Ordinateur portable"
prix = 999.99
quantite_stock = 25
en_promotion = True

print("Produit:", nom_produit)
print("Prix:", prix, "€")
print("Stock disponible:", quantite_stock)
print("En promotion:", en_promotion)
