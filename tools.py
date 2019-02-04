#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:15:27 2019

@author: 3602824
"""

class SuperState(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
    @property
    def ball(self):
        return self.state.ball.position
    
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position
    
    @property 
    #tuple
    def goal(self):
        if self.id_team == 1:
            return SoccerAction()
        else:
            return 