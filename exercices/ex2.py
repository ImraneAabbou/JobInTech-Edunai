# 1. Utilisez une boucle `for` pour compter combien de notes dans `notes_avis` sont positives (4 ou 5).
# 2. Créez une nouvelle liste appelée `avis_positifs` et ajoutez-y uniquement les notes positives.
# 3. Affichez le nombre total d'avis positifs et la nouvelle liste.
notes_avis = [5, 4, 2, 5, 3, 4, 1, 5]

avis_positifs = []
for note in notes_avis:
    if note >= 4:
        avis_positifs.append(note)

print(f"Nombre total d'avis positifs : {len(avis_positifs)}")
print(f"Avis positifs : {avis_positifs}")

