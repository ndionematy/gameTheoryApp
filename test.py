def bataille_des_sexes(choix_homme, choix_femme, gains=None):
    """
    Simule le jeu de la bataille des sexes.
    
    :param choix_homme: Choix de l'homme ('A' ou 'B')
    :param choix_femme: Choix de la femme ('A' ou 'B')
    :param gains: Dictionnaire des gains pour chaque combinaison de choix.
                  Si None, utilise les valeurs par défaut.
    :return: Un tuple contenant les gains de l'homme et de la femme
    """
    # Définir les gains par défaut
    if gains is None:
        gains = {
            ('A', 'A'): (3, 2),  # Gains si les deux vont à l'opéra
            ('A', 'B'): (0, 0),  # Homme va à l'opéra, femme va au football
            ('B', 'A'): (1, 1),  # Homme va au football, femme va à l'opéra
            ('B', 'B'): (2, 3)   # Gains si les deux vont au football
        }
    
    # Retourner les gains en fonction des choix des joueurs
    return gains[(choix_homme, choix_femme)]

# Exemple d'utilisation de la fonction
resultat = bataille_des_sexes('A', 'B')
print(f"Gains : Homme = {resultat[0]}, Femme = {resultat[1]}")

# Exemple avec des gains personnalisés
gains_personnalises = {
    ('A', 'A'): (5, 4),
    ('A', 'B'): (0, 0),
    ('B', 'A'): (2, 1),
    ('B', 'B'): (3, 5)
}

resultat_personnalise = bataille_des_sexes('B', 'A', gains=gains_personnalises)
print(f"Gains personnalisés : Homme = {resultat_personnalise[0]}, Femme = {resultat_personnalise[1]}")
