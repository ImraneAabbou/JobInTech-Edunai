# Créez une fonction paiement_ecommerce(articles, taux_taxe, code_reduction=''). où articles est une liste de dictionnaires {'nom': 'Produit', 'prix': 100, 'quantite': 1}. taux_taxe est un décimal (par ex., 0.05 pour 5%). code_reduction est une chaîne de caractères facultative ('SAVE10' pour 10% ou 'FREESHIP').
#La fonction doit :
#1. Calculer le sous-total de tous les articles.
#2. Appliquer une réduction : si 'SAVE10', 10% de réduction sur le sous-total ; si 'FREESHIP', la livraison est gratuite (considérez 5€ de frais de livraison par défaut, à annuler).
#3. Ajouter la taxe au sous-total réduit.
# 4. Retourner le total final (formaté à 2 décimales) et la réduction appliquée (par ex., '10% de réduction', 'Livraison gratuite', ou 'Aucune').
# Testez avec articles = [{'nom': 'Livre', 'prix': 20, 'quantite': 2}, {'nom': 'Stylo', 'prix': 5, 'quantite': 5}], taux_taxe = 0.07 et avec/sans codes de réduction.
#💡 Utilisez une boucle for pour le sous-total. Des if/elif pour la logique de réduction. Retournez un tuple de deux valeurs.

# Créez une fonction paiement_ecommerce(articles, taux_taxe, code_reduction='').
# où articles est une liste de dictionnaires {'nom': 'Produit', 'prix': 100, 'quantite': 1}.
# taux_taxe est un décimal (par ex., 0.05 pour 5%).
# code_reduction est une chaîne de caractères facultative ('SAVE10' pour 10% ou 'FREESHIP').
# La fonction doit :
# 1. Calculer le sous-total de tous les articles.
# 2. Appliquer une réduction : si 'SAVE10', 10% de réduction sur le sous-total ; si 'FREESHIP', la livraison est gratuite (considérez 5€ de frais de livraison par défaut, à annuler).
# 3. Ajouter la taxe au sous-total réduit.
# 4. Retourner le total final (formaté à 2 décimales) et la réduction appliquée (par ex., '10% de réduction', 'Livraison gratuite', ou 'Aucune').
# Testez avec articles = [{'nom': 'Livre', 'prix': 20, 'quantite': 2}, {'nom': 'Stylo', 'prix': 5, 'quantite': 5}], taux_taxe = 0.07 et avec/sans codes de réduction.

def paiement_ecommerce(articles, taux_taxe, code_reduction=''):
    sous_total = 0
    for article in articles:
        sous_total += article['prix'] * article['quantite']
    
    frais_livraison = 5
    reduction = 'Aucune'
    
    if code_reduction == 'SAVE10':
        sous_total *= 0.9
        reduction = '10% de réduction'
    elif code_reduction == 'FREESHIP':
        frais_livraison = 0
        reduction = 'Livraison gratuite'
    
    total = sous_total + frais_livraison
    total *= (1 + taux_taxe)
    
    return round(total, 2), reduction

# Tests
articles = [{'nom': 'Livre', 'prix': 20, 'quantite': 2}, {'nom': 'Stylo', 'prix': 5, 'quantite': 5}]
taux_taxe = 0.07

print(paiement_ecommerce(articles, taux_taxe))
print(paiement_ecommerce(articles, taux_taxe, 'SAVE10'))
print(paiement_ecommerce(articles, taux_taxe, 'FREESHIP'))

