#    Créez une liste de priorités [Normal, Urgent, Express, Standard, Rush]
#    Déplacez tous les articles 'Urgent' et 'Rush' au début de la liste
#    Affichez la liste de priorités finale organisée

priorities = ["Normal", "Urgent", "Express", "Standard", "Rush"]

priorities.remove("Urgent")
priorities.insert(0, "Urgent")

priorities.remove("Rush")
priorities.insert(1, "Rush")

print(priorities)
