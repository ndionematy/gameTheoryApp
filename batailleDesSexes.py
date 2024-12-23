import numpy as np

class GameTheory:
    def __init__(self, players, payoff_matrix):
        # Liste des joueurs
        self.players = players  
        
        # Matrice des gains
        self.payoff_matrix = payoff_matrix 
        
        # Définir les stratégies
        # self.strategies = strategies
        # self.nstrategies = len(strategies) 

    def display_payoff_matrix(self):
        print("Matrice des gains :")
        print(self.payoff_matrix)
        
    def get_strategies(self):
        # Retourner les stratégies possibles pour chaque joueur
        return [strategy for strategy in self.payoff_matrix.keys()]
        
    def find_nash_equilibrium(self):
        # Implémenter l'algorithme pour trouver l'équilibre de Nash
        pass

# Exemple pour le dilemme du prisonnier :
prisoner_game = GameTheory(
    players=["Joueur 1", "Joueur 2"],
    payoff_matrix=np.array([[(3, 3), (0, 5)], [(5, 0), (1, 1)]]))  # Matrice des gains
prisoner_game.display_payoff_matrix()
