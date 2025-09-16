# 1. Parcourez la liste `notes_tests`.
# 2. Trouvez la première note inférieure à 60.
# 3. Lorsque vous la trouvez, affichez un message comme `Première note échouée : 55` et arrêtez immédiatement la boucle.
# 4. Utilisez l'instruction `break`.
# Données : `notes_tests = [88, 92, 75, 55, 95, 45, 89]`
# 💡 La condition `if note < 60:` est ce dont vous avez besoin pour déclencher le `break`.

notes_tests = [88, 92, 75, 55, 95, 45, 89]

for note in notes_tests:
    if note < 60:
        print(f"Première note échouée : {note}")
        break

