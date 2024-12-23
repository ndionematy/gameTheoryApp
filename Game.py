class Game:
    def __init__(self, name, strategies, payoff_matrix, game_type):
        """
        Initialisation du jeu.
        :param name: Nom du jeu
        :param strategies: Liste des stratégies possibles pour chaque joueur
        :param payoff_matrix: Matrice des gains
        :param game_type: Type du jeu (statique ou dynamique)
        """
        self.name = name
        self.strategies = strategies
        self.payoff_matrix = payoff_matrix
        self.game_type = game_type

    def display_info(self):
        """Affiche les informations sur le jeu."""
        return {
            "name": self.name,
            "strategies": self.strategies,
            "payoff_matrix": self.payoff_matrix,
            "game_type": self.game_type
        }

    def compute_equilibria(self):
        """
        Calcule les équilibres de Nash pour un jeu statique.
        Compatible avec n'importe quel nombre de stratégies.
        """
        equilibria = []
        n_strategies_1 = len(self.strategies[0])
        n_strategies_2 = len(self.strategies[1])
        
        for i in range(n_strategies_1):
            for j in range(n_strategies_2):
                if self.is_best_response(i, j):
                    equilibria.append((self.strategies[0][i], self.strategies[1][j]))
        return equilibria

    def is_best_response(self, i, j):
        """
        Vérifie si un choix est une meilleure réponse pour les deux joueurs.
        :param i: Index de la stratégie du joueur 1
        :param j: Index de la stratégie du joueur 2
        """
        n_strategies_1 = len(self.strategies[0])
        n_strategies_2 = len(self.strategies[1])
        
        # Vérification pour le joueur 1
        player1_best = True
        for k in range(n_strategies_1):
            if self.payoff_matrix[k][j][0] > self.payoff_matrix[i][j][0]:
                player1_best = False
                break

        # Vérification pour le joueur 2
        player2_best = True
        for l in range(n_strategies_2):
            if self.payoff_matrix[i][l][1] > self.payoff_matrix[i][j][1]:
                player2_best = False
                break

        return player1_best and player2_best

    def simulate(self, player_choices):
        """
        Simule une partie en fonction des choix des joueurs.
        :param player_choices: Dictionnaire des choix des joueurs {1: choix_j1, 2: choix_j2}
        :return: Résultats des gains pour chaque joueur
        """
        try:
            player1_choice = self.strategies[0].index(player_choices[1])
            player2_choice = self.strategies[1].index(player_choices[2])
            return self.payoff_matrix[player1_choice][player2_choice]
        except (ValueError, KeyError, IndexError) as e:
            raise ValueError("Choix de stratégie invalide") from e

    def get_strategy_count(self):
        """
        Retourne le nombre de stratégies pour chaque joueur
        """
        return len(self.strategies[0]), len(self.strategies[1])