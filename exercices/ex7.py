#    Créez une variable `entree_formulaire` avec la valeur '' (une chaîne vide)
#    Évaluez la valeur booléenne de `entree_formulaire` en utilisant `bool()`
#    Affichez le résultat (qui sera `False` car la chaîne est vide)
#
#💡 Les chaînes vides et le nombre 0 sont considérés comme 'Falsey'


entree_formulaire = ''
is_valid = bool(entree_formulaire)

print("is valid:", is_valid)
