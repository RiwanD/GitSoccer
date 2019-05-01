    # -*- coding: utf-8 -*-
from .__init__ import soccersimulator
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import settings
GAME_WIDTH = 150
GAME_HEIGHT = 90
GAME_GOAL_HEIGHT = 10
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65

class superstate(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
    
#    def __getattr__(self, attr):
#       return getattr(self.state, attr)
        #
# Balle
    @property
    def ball(self):
        return self.state.ball.position
    @property
    def dist(self):
        return superstate.position - (superstate.ball)        
    """
    @property
    def trajectoire(self):
        return Vector2D(superstate.cage_adv_x - superstate.position.x, superstate.cage_adv_y - superstate.position.y )
    """    
    @property
    def near_ball(self):
        joueurs = [self.state.state_player(id_team, id_player).position for (id_team, id_player) in self.state.players]
        return min([(self.player.playerstate(self.ball), player) for player in joueurs])
    

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
    def to_ball(self):
        return Vector2D(self.ball.x - self.position.x, self.ball.y - self.position.y)

    @property
    def to_goal(self):
        return Vector2D(self.cage_adv - self.position)

    
    def def_ramos(self):
        if self.id_team == 1:
            return Vector2D((self.ball.x - GAME_WIDTH/2)/2, (self.ball.y - GAME_HEIGHT/2)/2)
        else:
            return Vector2D((self.ball.x)/2, (self.ball.y - GAME_HEIGHT/2)/2)

    
    @property
    def shoot_possible(self):
        pass

#Equpier 

    @property
    def mate(self):
        return [self.state.state_player(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team == self.id_team]
        
    @property
    def near_mate(self):
        mate = self.mate
        return min([(self.player.position.distance(player), player) for player in mate])
    
    @property
    def near_mate_ball(self):
        mate = self.mate
        return min([(self.player.playerstate(self.ball), player) for player in mate])
# Adversaire

    @property
    def opponents(self):
        return [self.state.state_player(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]

    @property
    def opponents_front(self):
        opp = self.opponents
        if superstate.team == 1:
            return [self.state.state_player(id_team, id_player).position for (id_team, id_player) in opp 
            if self.state.state_player(id_team, id_player).position.x < self.position.x]
        else:
            return [self.state.state_player(id_team, id_player).position for (id_team, id_player) in opp 
            if self.state.state_player(id_team, id_player).position.x > self.position.x]
    
    @property
    #retourne la liste des opposant présents dans le rectangle défini entre le joueur et les cages adverses 
    def opponents_rect(self):
        opp_f = self.opponents_front
        return [self.state.state_player(id_team, id_player) for (id_team, id_player) in opp_f 
        if (self.state.state_player(id_team, id_player).position.y < (self.position.y + 2)) 
        and (self.state.state_player(id_team, id_player).position.y > (self.position.y - 2))]

    @property
    def near_opp(self):
        opponents = self.opponents
        return min([(self.player.distance(player), player) for player in opponents])
    
    @property
    def near_opp_ball(self):
        opponents = self.opponents
        return min([(self.player.playerstate(self.ball), player) for player in opponents])
# Terrain
    @property
    def cage(self):
        if self.state.player_state(self.id_team) == 1:
            return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
        else:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)
    
    @property
    def cage_adv(self):
        if self.state.player_state(self.id_team) == 1:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)
        else:
            return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
    """
    @property
    def cage_adv_x(self):
        return superstate.cage_adv()[1]
        
    @property
    def cage_adv_y(self):
        return self.cage_adv()[2]
    """
    @property
    def cage_def(self):
        if self.state.player_state(self.id_team) == 1:
            return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
        else:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)
    @property
    def top_corner_left(self):
        return Vector2D(0,90)
    
    @property
    def top_corner_right(self):
        return Vector2D(150,90) 
    
    @property
    def bottom_corner_left(self):
        return Vector2D(150,0)
        
    @property
    def bottom_corner_right(self):
        return Vector2D(0,0)
    
    @property
    def centre(self):
        return (GAME_WIDTH/2,GAME_HEIGHT/2)

