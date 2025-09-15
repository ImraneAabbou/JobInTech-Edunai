#     Étant donné un `solde_compte` et un `montant_retrait`, vérifiez si le solde est suffisant.
#     Si oui, affichez le nouveau solde. Sinon, affichez un message 'Fonds insuffisants'.
#
# 💡 Un simple bloc `if/else` est parfait pour cela.

solde_compte = 100
montant_retrait = 10

if (nouveau_solde := (solde_compte - montant_retrait)) >= 0:
    print('Nouveau_solde:', nouveau_solde)
else:
    print("Fonds insuffisants")
