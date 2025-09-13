#    Créez une liste de 6 numéros de commande (CMD001, CMD002, CMD003, CMD004, CMD005, CMD006)
#    Traitez les 3 premières commandes (retirez-les de la liste)
#    Affichez les commandes restantes en attente de traitement
#
#💡 Utilisez del ou pop() pour retirer des éléments du début de la liste

numbers = ["CMD001", "CMD002", "CMD003", "CMD004", "CMD005", "CMD006"]

print(
    "first elements:",
    numbers.pop(0),
    numbers.pop(1),
    numbers.pop(2),
)


print("rest en attente:", numbers)
