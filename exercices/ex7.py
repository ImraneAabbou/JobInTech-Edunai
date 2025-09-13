#    Créez une liste de scores de satisfaction [4.2, 3.8, 4.9, 3.5, 4.7, 4.1, 3.9]
#    Comptez combien de scores sont supérieurs à 4.0
#    Trouvez le score le plus élevé et le plus bas


satisfaction_scores = [4.2, 3.8, 4.9, 3.5, 4.7, 4.1, 3.9]
high_scores = list(filter(lambda x: x > 4, satisfaction_scores))

print("scores supérieurs a 4:", high_scores, f"; {len(high_scores)} score(s)")
