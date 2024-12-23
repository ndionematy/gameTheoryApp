from Game import Game
import numpy as np

class CustomStaticGame(Game):
    def __init__(self):
        """Initialisation avec des valeurs par défaut"""
        super().__init__(
            name="Jeu Personnalisé",
            strategies=[["Stratégie 1", "Stratégie 2"], ["Stratégie 1", "Stratégie 2"]],
            payoff_matrix=[
                [[0, 0], [0, 0]],
                [[0, 0], [0, 0]]
            ],
            game_type="statique personnalisé"
        )
        self.player_names = ["Joueur 1", "Joueur 2"]

    def update_configuration(self, strategies, payoff_matrix):
        """Met à jour la configuration du jeu"""
        self.strategies = strategies
        self.payoff_matrix = payoff_matrix

    def find_dominant_strategies(self):
        """
        Trouve les stratégies dominantes pour chaque joueur
        Retourne un dictionnaire avec les stratégies dominantes par joueur
        """
        dominant_strategies = {
            "Joueur 1": {"strict": [], "weak": []},
            "Joueur 2": {"strict": [], "weak": []}
        }

        # Pour le Joueur 1
        for i in range(len(self.strategies[0])):
            strict_dominant = True
            weak_dominant = True
            for k in range(len(self.strategies[0])):
                if i != k:
                    for j in range(len(self.strategies[1])):
                        if self.payoff_matrix[i][j][0] < self.payoff_matrix[k][j][0]:
                            strict_dominant = False
                        if self.payoff_matrix[i][j][0] <= self.payoff_matrix[k][j][0]:
                            weak_dominant = False

            if strict_dominant:
                dominant_strategies["Joueur 1"]["strict"].append(self.strategies[0][i])
            elif weak_dominant:
                dominant_strategies["Joueur 1"]["weak"].append(self.strategies[0][i])

        # Pour le Joueur 2
        for j in range(len(self.strategies[1])):
            strict_dominant = True
            weak_dominant = True
            for l in range(len(self.strategies[1])):
                if j != l:
                    for i in range(len(self.strategies[0])):
                        if self.payoff_matrix[i][j][1] < self.payoff_matrix[i][l][1]:
                            strict_dominant = False
                        if self.payoff_matrix[i][j][1] <= self.payoff_matrix[i][l][1]:
                            weak_dominant = False

            if strict_dominant:
                dominant_strategies["Joueur 2"]["strict"].append(self.strategies[1][j])
            elif weak_dominant:
                dominant_strategies["Joueur 2"]["weak"].append(self.strategies[1][j])

        return dominant_strategies

    def display_info(self):
        """Surcharge de la méthode d'affichage des informations"""
        return {
            "name": self.name,
            "game_type": self.game_type,
            "strategies": self.strategies,
            "payoff_matrix": self.payoff_matrix
        }