# Écrivez du code pour effectuer les tâches suivantes :
#
#     Étant donné un `total_historique_achats`, attribuez un niveau : 'Bronze' pour <100€, 'Argent' pour 100€-500€, 'Or' pour >500€.
#
# 💡 L'ordre de vos conditions `if/elif` est important.

total_historique_achats = 320

if total_historique_achats < 100:
    niveau = "Bronze"
elif total_historique_achats <= 500:
    niveau = "Argent"
else:
    niveau = "Or"

print(niveau)

