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

# Balle
    @property
    def ball(self):
        return self.state.ball.position
# Joueur
    @property
    def team(self):
        return self.state.player_state(self.id_team)

    @property
    def position(self):
        return self.state.player_state(self.id_team, self.id_player).position

    @property
    def player(self):
		return self.state.state_player(self.id_team, self.id_player)
    
    @property
    def vitesse(self):
        return self.state.player_state(self.id_team, self.id_player).vitesse

	@property
	def nearest(self):
		return [(player, position) for 

#Equpier 

	@property
	def mate(self):
		return [self.state.state_player(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team == self.id_team]
		
	@property
	def near_mate(self):
		return min([(self.player.position.distance(player), player) for player in mate])

# Adversaire

    @property
    def opponents(self):
		return [self.state.state_player(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
	
	@property
	def near_opp(self):
		return min([(self.player.distance(player), player) for player in opponents])

# Terrain
    @property
    def cage(self):
        if self.state.player_state(self.id_team) == 1:
            return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
        else:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)
    
    @property
    def cage_def(self):
        if self.state.player_state(self.id_team) == 1:
            return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
        else:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)
    
        
