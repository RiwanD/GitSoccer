# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:10:15 2019

@author: lepet
"""

from soccersimulator import stategy, settings



def Superstate(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_player = id_player
        self.id_team = id_team
