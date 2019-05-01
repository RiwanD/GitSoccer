# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet.actions import Action, Move, Shoot
from projet.tools import superstate


if __name__  == "__main__":
    team1 = SoccerTeam(name="Team 1")
    team2 = SoccerTeam(name="Team 2")


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(),
                            Vector2D.create_random())

"""class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")

    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball(superstate.to_ball) + shoot.to_goal()
"""
class Defenseur2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.def_Ramos(s)



class booba(Strategy):
    def __init__(self):
        Strategy.__init__(self, "booba")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        teta = -(state.player_state(1,0).position.x)*(state.ball.position.x)+(state.player_state(1,0).position.y)*(state.ball.position.y)
        angle = (state.player_state(1,0).position.x - 150), (state.player_state(1,0).position.y)
        if id_team == 1:
            return SoccerAction(state.ball.position-state.player_state(1, 0).position,
                   state.ball.position-state.player_state(1 ,0).position * teta)
        else:
            return SoccerAction(state.ball.position-state.player_state(2, 0).position,
                   state.ball.position-state.player_state(2 ,0).position * teta)

class Def(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        if id_team == 1:
            return s.def_ramos
    # Add players
    team1.add("Ramos", Def())
#    team1.add("RR", Def())
    team2.add("CR7", booba())   

    # Create a match
    simu = Simulation(team1, team2)

    # Simulate and display the match
    show_simu(simu)

