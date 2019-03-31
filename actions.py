# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 10:34:00 2019

@author: lepet
"""
from soccersimulator import setting, utils, stategies, events, mdpsoccer, matches, superstate, tools
from tools import *

class Move(object):
    def __init__(self, superstate):
        self.superstate = superstate
        
    def move(self, acceleration=None):
        return SoccerAction(acceleration= acceleration)
    
#En attaque
    def to_ball(self):
        return self.move(self.superstate.ball_dir())
        
    def passe(self):
		if dist < PLAYER_RADIUS + BALL_RADIUS && 
		return SoccerAction(
        
    
    

    
#En defense
        
        
class shoot(object):
    def __init__(self, superstate):
        self.superstate = superstate

    def shoot(self, direction=None):
        if dist < PLAYER_RADIUS + BALL_RADIUS:
             return SoccerAction(shoot=direction)
        else:
             return SoccerAction()
#Seul
    def to_goal(self, strenght = None):
        return self.shoot(self.superstate.goal_dir)
                  
    def __init__(self, superstate):
        self.superstate = superstate
        
class passe(object):
    def __init__(self, superstate):
        self.superstate = superstate

    def passe(self, direction= None):
        dist = self.superstate.player.distance(self.superstate.ball)
        n1 = near opp
        if dist  < PLAYER_RADIUS + BALL_RADIUS:
             return SoccerAction(pass=direction)
        else:
             return SoccerAction()

#En equipe
        
    def near_opp(self):
        opp = [self.state.player(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
        
        return min([(self.player.disctance(player), player) for player in opp])[1]
    
