# test1.py
import streamlit as st
from Game import Game
from games.jeux_statique_general import CustomStaticGame

# Initialisation des jeux
dilemme_prisonnier = Game(
    name="Dilemme du Prisonnier",
    strategies=[["Coopérer", "Défaut"], ["Coopérer", "Défaut"]],
    payoff_matrix=[
        [[3, 3], [0, 5]],
        [[5, 0], [1, 1]]
    ],
    game_type="statique"
)

chicken_game = Game(
    name="Chicken Game",
    strategies=[["Droit", "Tourner"], ["Droit", "Tourner"]],
    payoff_matrix=[
        [[-1, -1], [2, 0]],
        [[0, 2], [1, 1]]
    ],
    game_type="statique"
)

custom_game = CustomStaticGame()

# Dictionnaire des jeux
games = {
    "Dilemme du Prisonnier": dilemme_prisonnier,
    "Chicken Game": chicken_game,
    "Jeu Personnalisé": custom_game
}

# Dictionnaire des images associées aux jeux
game_images = {
    "Dilemme du Prisonnier": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Prisoner%27s_Dilemma_Payoff_Matrix.svg/512px-Prisoner%27s_Dilemma_Payoff_Matrix.svg.png",
    "Chicken Game": "https://vivifychangecatalyst.files.wordpress.com/2015/06/chicken-2.jpg",
    "Jeu Personnalisé": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Game_Theory.svg/640px-Game_Theory.svg.png"
}

# Configuration de la page Streamlit
st.set_page_config(page_title="Théorie des Jeux", layout="wide")

# Barre latérale pour choisir un jeu
st.sidebar.title("📚 Sélectionnez un Jeu")
game_choice = st.sidebar.selectbox("Liste des jeux :", list(games.keys()))
selected_game = games[game_choice]

# Interface spécifique pour le jeu personnalisé
if game_choice == "Jeu Personnalisé":
    st.title("🎮 Configuration du Jeu Personnalisé")
    
    # Configuration des joueurs
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔹 Joueur 1")
        n_strategies_1 = st.number_input("Nombre de stratégies (J1)", 2, 5, 2, key="n_strat_1")
        strategies_1 = []
        for i in range(n_strategies_1):
            strat = st.text_input(f"Stratégie {i+1} (J1)", f"Stratégie {i+1}", key=f"strat1_{i}")
            strategies_1.append(strat)

    with col2:
        st.subheader("🔸 Joueur 2")
        n_strategies_2 = st.number_input("Nombre de stratégies (J2)", 2, 5, 2, key="n_strat_2")
        strategies_2 = []
        for i in range(n_strategies_2):
            strat = st.text_input(f"Stratégie {i+1} (J2)", f"Stratégie {i+1}", key=f"strat2_{i}")
            strategies_2.append(strat)

    # Matrice des gains
    st.subheader("📊 Matrice des gains")
    payoff_matrix = []
    
    for i in range(n_strategies_1):
        row = []
        for j in range(n_strategies_2):
            st.write(f"Gains pour {strategies_1[i]} vs {strategies_2[j]}")
            col1, col2 = st.columns(2)
            with col1:
                gain_j1 = st.number_input(f"Gain J1", key=f"gain1_{i}_{j}")
            with col2:
                gain_j2 = st.number_input(f"Gain J2", key=f"gain2_{i}_{j}")
            row.append([gain_j1, gain_j2])
        payoff_matrix.append(row)

    if st.button("Mettre à jour le jeu"):
        custom_game.update_configuration([strategies_1, strategies_2], payoff_matrix)
        st.success("Jeu mis à jour avec succès!")

# Affichage standard pour tous les jeux
st.image(game_images[game_choice], caption=f"Illustration : {game_choice}", use_column_width=True)

# Informations sur le jeu
st.subheader("🧩 Informations sur le Jeu")
info = selected_game.display_info()
st.markdown(f"**Nom :** {info['name']}")
st.markdown(f"**Type :** {info['game_type']}")
st.markdown("**Stratégies possibles :**")
st.write(info['strategies'])

# Fonction pour afficher la matrice des gains
def render_payoff_matrix(matrix, strategies):
    styled_matrix = f"""
    <style>
        .styled-table {{
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 18px;
            text-align: center;
        }}
        .styled-table th,
        .styled-table td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        .styled-table th {{
            background-color: #f4f4f4;
        }}
    </style>
    <table class="styled-table">
        <tr>
            <th>Joueur 1 / Joueur 2</th>
            <th>{strategies[1][0]}</th>
            <th>{strategies[1][1]}</th>
        </tr>
        <tr>
            <th>{strategies[0][0]}</th>
            <td>{matrix[0][0]}</td>
            <td>{matrix[0][1]}</td>
        </tr>
        <tr>
            <th>{strategies[0][1]}</th>
            <td>{matrix[1][0]}</td>
            <td>{matrix[1][1]}</td>
        </tr>
    </table>
    """
    return styled_matrix

# Affichage de la matrice des gains
st.markdown("**Matrice des gains actuelle :**")
st.markdown(render_payoff_matrix(info['payoff_matrix'], info['strategies']), unsafe_allow_html=True)

# Simulation
st.subheader("🎲 Simulation")
col5, col6 = st.columns(2)

with col5:
    player1_choice = st.selectbox("🔹 Choix du Joueur 1 :", selected_game.strategies[0])
with col6:
    player2_choice = st.selectbox("🔸 Choix du Joueur 2 :", selected_game.strategies[1])

if st.button("Simuler"):
    result = selected_game.simulate({1: player1_choice, 2: player2_choice})
    st.success(f"Résultats : Joueur 1 = {result[0]}, Joueur 2 = {result[1]}")

# Analyse des stratégies
st.subheader("📊 Analyse du jeu")
col7, col8 = st.columns(2)

with col7:
    if st.button("Afficher les équilibres de Nash"):
        equilibria = selected_game.compute_equilibria()
        if equilibria:
            st.write("**Équilibres trouvés :**")
            for eq in equilibria:
                st.write(eq)
        else:
            st.warning("Aucun équilibre trouvé.")

with col8:
    if game_choice == "Jeu Personnalisé" and st.button("Analyser les stratégies dominantes"):
        dominant_strategies = custom_game.find_dominant_strategies()
        for player, strategies in dominant_strategies.items():
            st.write(f"**{player}:**")
            if strategies["strict"]:
                st.success(f"Stratégies strictement dominantes : {', '.join(strategies['strict'])}")
            if strategies["weak"]:
                st.warning(f"Stratégies faiblement dominantes : {', '.join(strategies['weak'])}")
            if not strategies["strict"] and not strategies["weak"]:
                st.info("Aucune stratégie dominante")