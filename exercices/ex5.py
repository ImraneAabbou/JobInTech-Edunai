# 1. Définir la fonction formater_adresse(rue, ville, code_postal).
# 2. Retourner une chaîne multi-lignes avec f-string : rue \n ville, code_postal.
# 3. Tester avec '123 Rue Principale', 'Paris', '75001'.
# 4. Afficher le résultat.

def formater_adresse(rue, ville, code_postal):
    return f"{rue}\n{ville}, {code_postal}"

# Test
adresse = formater_adresse("123 Rue Principale", "Paris", "75001")
print(adresse)

