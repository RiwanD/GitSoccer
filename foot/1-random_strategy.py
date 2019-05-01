# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet import actions, tools
from tools import *
from actions import *


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(),
                            Vector2D.create_random())

class Defenseur(Strategy):
    def __init__(Self):
        Strategy.__init__(Self, "Defenseur")
    
    def compute_strategy (self, state, id_team, id_player):
        if self.player.player_state(self.id_team) == 1:
            if (self.superstate.near_opp_ball <= self.superstate.near_mate_ball):
                nopp = self.superstate.near_opp
                if nopp[1].position.x < self.superstate.position.x:
                    return so.SoccerAction(nopp[1].position.x - 5, shoot = None)

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Random", RandomStrategy())  # Random strategy
team2.add("Defenseur", Defenseur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
