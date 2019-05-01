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
        return move.def_Ramos()

class Def(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.def_Ramos(def_Ramos)

    # Add players
    team1.add("Ramos", Defenseur2())
    team1.add("RR", Def())
    team2.add("CR7", RandomStrategy())   

    # Create a match
    simu = Simulation(team1, team2)

    # Simulate and display the match
    show_simu(simu)

