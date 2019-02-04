#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:25:51 2019

@author: 3602824
"""
class Move(object):
    def __init__(self, superstate):
        self.superstate = superstate
        
    def move(seflf, acceleration=None):
        return SoccerAction(acceleration= acceleration)
    
#En attaque
    def to_ball(self):
        return self.move(self.superstate.ball_dir())
        
        
    
    
    
#En defense
        
        
class shoot(object):
    def __init__(self, superstate):
        self.superstate = superstate

    def shoot(self, direction=None):
        dist = self.superstate.player.distance(self.superstate.ball)
        if dist < PLAYER_RADIUS + BALL_RADIUS:
             return SoccerAction(shoot=direction)
        else:
             return SoccerAction()
#Seul
    def to_goal(self, strenght = None):
        return self.shoot(self.superstate.goal_dir)
                  

#En equipe
        
    def near_opp(self):
        opp = [self.state.player(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
        
        return min([(self.player.disctance(player), player) for player in opp])[1]
    