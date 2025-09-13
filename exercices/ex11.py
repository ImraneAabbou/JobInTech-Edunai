#Créez des listes pour titres_films ['Héros d'Action', 'Histoire d'Amour', 'Soirée Comédie'], horaires ['19h00', '21h30', '18h00'], sieges_disponibles [45, 23, 67], et prix_billets [12.50, 10.00, 8.50]
#Calculez les revenus totaux si tous les sièges sont vendus pour chaque film
#Trouvez quel film a le plus haut potentiel de revenus
#Déterminez le prix moyen des billets pour tous les films
#Créez une liste de réservation prioritaire triée par potentiel de revenus (le plus élevé en premier)

titres_films = ['Héros d\'Action', 'Histoire d\'Amour', 'Soirée Comédie']
horaires = ['19h00', '21h30', '18h00']
sieges_disponibles = [45, 23, 67]
prix_billets = [12.50, 10.00, 8.50]

revenues = list(
    map(
        lambda pair: pair[0] * pair[1],
        zip(
            prix_billets,
            sieges_disponibles
        )
    )
)

zipped_films_prices = sorted(zip(titres_films, prix_billets), key=lambda pair: pair[1], reverse=True)

[max_revenu_film_name, max_revenu_film_price] = zipped_films_prices[0]

prix_moyenne = sum(prix_billets) / len(prix_billets)

reservation_prioritaire = sorted(revenues, reverse=True)



print("Revenus potentiels par film :", revenues)
print(f"Le film avec le plus haut potentiel est '{max_revenu_film_name}' avec {max_revenu_film_price} €")
print("Prix moyen des billets :", round(prix_moyenne, 2))
print("Liste de réservation prioritaire :", reservation_prioritaire)
