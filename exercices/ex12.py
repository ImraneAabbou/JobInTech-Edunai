# Créez des listes pour noms_etudiants ['Alex', 'Beth', 'Carlos', 'Diana'], notes_test1 [85, 92, 78, 96], notes_test2 [88, 89, 82, 94], et notes_test3 [90, 87, 85, 92]
# Calculez la note moyenne de chaque étudiant sur les trois tests
# Identifiez les étudiants qui se sont améliorés du test 1 au test 3
# Trouvez la moyenne de classe pour chaque test
# Déterminez quel test a eu la meilleure performance de classe


noms_etudiants = ["Alex", "Beth", "Carlos", "Diana"]
notes_test1 = [85, 92, 78, 96]
notes_test2 = [88, 89, 82, 94]
notes_test3 = [90, 87, 85, 92]

etudiant_note_zipped = list(zip(noms_etudiants, notes_test1, notes_test2, notes_test3))

list(map(lambda e: print(f"{e[0]} -> {sum(e[1:]) / len(e[1:])}"), etudiant_note_zipped))
