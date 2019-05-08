from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet.actions import Action, Move, Shoot
from projet.tools import superstate
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIUS, GAME_HEIGHT, GAME_WIDTH
from sklearn.model_selection import ParameterGrid
from Grid import GoalSearch, GoTestStrategy2
from strategies import Def2v2


class Immobile(Strategy):
    def __init__(self, strength=None):
        Strategy.__init__(self, "Imm")
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_joueur = s.pos_joueur
        pos_ball = s.pos_ball
        if pos_ball.distance(pos_joueur) < PLAYER_RADIUS + BALL_RADIUS :
            return SoccerAction(Vector2D(3*GAME_WIDTH/4, GAME_WIDTH/2 + 2), shoot = None)
        else:
           return SoccerAction(acceleration = 0, shoot = None)





if __name__  == "__main__":
    team1 = SoccerTeam(name="Team 1")
    team2 = SoccerTeam(name="Team 2")

    # Add players
    team1.add("Test", GoTestStrategy2())
    team1.add("Immobile", Immobile())
    
    
    # Create a match
    simu = Simulation(team1, team2, max_steps = 400)

    # Simulate and display the match
    show_simu(simu)



expe = GoalSearch(strategy=GoTestStrategy2(), strategy2 = Immobile(), params={'strength': [4, 5]},trials = 30, max_round_step = 60)
expe.start(True)
print(expe.get_res())
print(expe.get_best())
print("Distance entre les joueurs: ", Vector2D(75, GAME_HEIGHT/2).distance(Vector2D(3*GAME_WIDTH/4, GAME_WIDTH/2)))
