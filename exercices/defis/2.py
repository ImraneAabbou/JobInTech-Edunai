# Créez une fonction evaluer_performance_employe(score, projets_termines, role='Junior').
# La fonction doit retourner un statut ('Excellent', 'Bon', 'Nécessite Amélioration') basé sur les critères suivants :
# - 'Excellent' : Si score > 90 ET projets_termines > 5.
# - 'Bon' : Si score > 70 ET projets_termines > 3.
# - 'Nécessite Amélioration' : Sinon.
# Pour un role 'Senior', les seuils sont plus élevés : 'Excellent' si score > 95 et projets > 7 ; 'Bon' si score > 85 et projets > 5.
# La fonction devrait également retourner un message de recommandation personnalisé basé sur le statut et le rôle.
# Testez avec différents scores, projets et rôles (Junior, Senior).

def evaluer_performance_employe(score, projets_termines, role='Junior'):
    if role == 'Junior':
        if score > 90 and projets_termines > 5:
            statut = 'Excellent'
            message = "Continuez ainsi, vous êtes un Junior très performant !"
        elif score > 70 and projets_termines > 3:
            statut = 'Bon'
            message = "Bon travail, continuez vos efforts pour progresser."
        else:
            statut = 'Nécessite Amélioration'
            message = "Travaillez sur vos compétences pour de meilleurs résultats."
    elif role == 'Senior':
        if score > 95 and projets_termines > 7:
            statut = 'Excellent'
            message = "Vous excellez dans votre rôle Senior, félicitations !"
        elif score > 85 and projets_termines > 5:
            statut = 'Bon'
            message = "Votre performance est bonne, continuez à viser l'excellence."
        else:
            statut = 'Nécessite Amélioration'
            message = "Renforcez vos compétences et votre gestion de projets."
    else:
        statut = 'Nécessite Amélioration'
        message = "Rôle non reconnu, impossible d'évaluer correctement."
    
    return statut, message


# Tests
print(evaluer_performance_employe(92, 6, 'Junior'))
print(evaluer_performance_employe(75, 4, 'Junior'))
print(evaluer_performance_employe(60, 2, 'Junior'))
print(evaluer_performance_employe(97, 8, 'Senior'))
print(evaluer_performance_employe(88, 6, 'Senior'))
print(evaluer_performance_employe(80, 4, 'Senior'))

