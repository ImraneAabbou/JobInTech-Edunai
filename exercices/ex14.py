#    Définissez `role_utilisateur` = 'editeur', `est_proprietaire_article` = `False`, `compte_verifie` = `True`
#    Un utilisateur peut modifier un article s'il est un 'admin' OU (s'il est un 'editeur' ET le propriétaire de l'article)
#    Assurez-vous que, dans tous les cas, le `compte_verifie` doit être `True` pour autoriser l'action
#💡 Utilisez des parenthèses pour regrouper la logique `or` : `(condition1 or condition2) and condition3`


role_utilisateur = 'editeur'
est_proprietaire_article = False
compte_verifie = True

peut_modifier_article = any([
    role_utilisateur == "admin",
    est_proprietaire_article,
]) and compte_verifie

print("peut modifier:", peut_modifier_article)
