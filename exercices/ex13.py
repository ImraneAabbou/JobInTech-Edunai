#    Définissez `longueur_piece` = 10.02, `largeur_piece` = 5.01, `poids_piece` = 2.55
#    Vérifiez si la pièce est dans les tolérances : longueur entre 9.9 et 10.1, largeur entre 4.9 et 5.1, ET poids < 2.6
#    Affichez `True` si toutes les conditions de qualité sont remplies, sinon `False`
#
#💡 Utilisez des comparaisons chaînées comme `9.9 <= longueur_piece <= 10.1`


longueur_piece = 10.02
largeur_piece = 5.01
poids_piece = 2.55


dans_tolerance = 9.9 < longueur_piece < 10.1
dans_tolerance = dans_tolerance and (4.9 < largeur_piece < 5.1)
dans_tolerance = dans_tolerance and poids_piece < 2.6

print(dans_tolerance)
