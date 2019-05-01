# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 10:38:07 2019

@author: lepet
"""

from . import strategies, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools import *
from .actions import *

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-1,1),
                            Vector2D.create_random(-1,1))
        
'''
class Defenseur (Strategy):
    def __init__(Self):
        Strategy.__init__(Self, "Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        if self.player.player_state(self.id_team) == 1:
            if (self.superstate.near_opp_ball <= self.superstate.near_mate_ball)
'''        
        
class booba(Strategy):
    def __init__(self):
        Strategy.__init__(self, "booba")
   
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        teta = (state.player_state(1,0).position.x)*(state.ball.position.x)+(state.player_state(1,0).position.y)*(state.ball.position.y)
        if (id_team)==1:
            return SoccerAction(state.ball.position-state.player_state(1 ,0).position,(state.ball.position-state.player_state(1 ,0).position)*teta)
        else:    
            return SoccerAction(state.ball.position-state.player_state(1 ,0).position,state.ball.position-state.player_state(1 ,0).position-teta)
                            


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("booba", booba())
team2.add("Random", RandomStrategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)

def __main__(self):
    pass
