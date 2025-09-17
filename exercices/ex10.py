# 1. Définir la variable globale compteur_actions = 0.
# 2. Créer la fonction incrementer_compteur() utilisant global pour modifier compteur_actions.
# 3. Incrémenter compteur_actions de 1 à chaque appel.
# 4. Appeler la fonction plusieurs fois et afficher compteur_actions après chaque appel.

compteur_actions = 0

def incrementer_compteur():
    global compteur_actions
    compteur_actions += 1

# Tests
incrementer_compteur()
print(compteur_actions)  # 1

incrementer_compteur()
print(compteur_actions)  # 2

incrementer_compteur()
print(compteur_actions)  # 3
