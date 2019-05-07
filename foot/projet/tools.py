    # -*- coding: utf-8 -*-
from .__init__ import soccersimulator
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import settings
from soccersimulator import utils
from . import utils

import math,random
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
    def pos_ball(self):
        return self.state.ball.position

    @property
    def vitesse_ball(self):
        return self.state.ball.vitesse
    @property
    def approxi_pos_ball(self):
        return self.pos_ball + 5 * self.state.ball.vitesse
      
    """
    @property
    def trajectoire(self):
        return Vector2D(superstate.cage_adv_x - superstate.position.x, superstate.cage_adv_y - superstate.position.y )
    """    
   
    @property
    def dist_joueur_ball(self):
        return self.pos_joueur.distance(self.pos_ball)


# Joueur
    @property
    def team(self):
        return self.id_team
    @property
    def pos_joueur(self):
        return self.state.player_state(self.id_team, self.id_player).position

   
    @property
    def joueur(self):
        return self.state.player_state(self.id_team, self.id_player)
    
    @property
    def vitesse_joueur(self):
        return self.state.player_state(self.id_team, self.id_player).vitesse

    @property
    def to_ball(self):
        return Vector2D(self.pos_ball.x - self.pos_joueur.x, self.pos_ball.y - self.pos_joueur.y)

    @property
    def to_ball2(self):
        return self.pos_ball - self.pos_joueur
    
    """
    @property
    def to_goal(self):
        return Vector2D(self.cage_adv - self.pos_joueur)
    """
    
    def def_ramos(self):
        if self.id_team == 1:
            return Vector2D((self.pos_ball.x - GAME_WIDTH/2)/2, (self.pos_ball.y - GAME_HEIGHT/2)/2)
        else:
            return Vector2D((self.pos_ball.x)/2, (self.pos_ball.y - GAME_HEIGHT/2)/2)

    @property
    def shoot_poss_light(self):
        return (self.pos_ball.distance(self.pos_joueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS)

    @property
    def appel_de_balle(self):
        roulette = random.random()
        if roulette >0.5:
            if self.id_team == 1:
                return Vector2D(7*GAME_WIDTH/10, 2*GAME_HEIGHT/3)
            else:
                return Vector2D(3*GAME_WIDTH/10, 2*GAME_HEIGHT/3)
        else:
            if self.team == 1:
                return Vector2D(7*GAME_WIDTH/10, GAME_HEIGHT/3)
            else:
                return Vector2D(3*GAME_WIDTH/10, GAME_HEIGHT/3)

#Equpier 

    @property
    def mate(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team == self.id_team and id_player != self.id_player]

    """
    def near_opp_ball(self):
        opponents =[self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
        near = min([(self.player.position.distance(self.pos_ball), player) for player in opponents])
        return near
    """
    @property
    def near_mate(self):
        mate = self.mate
        near = min([(player.distance(self.pos_joueur), player) for player in mate])
        (dist, jou) = near
        this_one = jou
        return near
    
    @property
    def mate_front(self):
        mates = self.mate
        if self.team == 1:
            return [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x > self.pos_joueur.x and id_team == self.id_team]
        else:
            return [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x < self.pos_joueur.x and id_team == self.id_team]
    
    @property
    def near_mate_ball(self):
        mate = self.mate
        return min([player.distance(self.pos_ball) for player in mate])
# Adversaire

    @property
    #retourne la position de tous les joueurs sur le terrain
    def pos_joueurs_all(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players]

    @property
    def near_ball(self):
        joueurs = self.pos_joueurs_all
        near = min([(player.distance(self.pos_ball), player) for player in joueurs])
        return near

    @property
    #retourne la position des advrsaires
    def opponents_pos(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
    
    @property
    #retourne la position des advrsaires
    def opponents(self):
        return [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players if id_team != self.id_team]

    @property
    def opponents_front_pos(self):
        opp = self.opponents_pos
        if self.team == 1:
            return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in opp 
            if self.state.player_state(id_team, id_player).position.x > self.pos_joueur.x]
        else:
            return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in opp 
            if self.state.player_state(id_team, id_player).position.x < self.pos_joueur.x]

    @property
    def opponents_front(self):
        opp = self.opponents
        if self.team == 1:
            return [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x > self.pos_joueur.x and id_team != self.id_team]
        else:
            return [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x < self.pos_joueur.x and id_team != self.id_team]
    
    @property
    def passe_poss(self):
        mate_f = self.mate_front
        if mate_f != []:
            return True
        return False

    def shoot_poss(self, pos_joueur, aimed_pos):
        #opp_f = self.opponents_front
        vect_exp_shoot = aimed_pos - pos_joueur
        dist_exp_shoot_norm =pos_joueur.distance(aimed_pos)
        if self.team == 1:
            contreurs_pot = [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x > self.pos_joueur.x and id_team != self.id_team]
        else: 
            contreurs_pot = [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x < self.pos_joueur.x and id_team != self.id_team]

        dist_joueur_contreurs = [pos_joueur.distance(player) for player in contreurs_pot]
        dist_aimed_pos_contreur = [aimed_pos.distance(player) for player in contreurs_pot]
        dist_totale = [i+j for i,j in zip(dist_joueur_contreurs, dist_aimed_pos_contreur)]
        if (dist_totale != []):
            if dist_exp_shoot_norm*1.3 >= min(dist_totale):
                return True
            else:
                return False
        return True
    @property
    def bonne_zone(self):
        if self.team == 1:
            if self.pos_joueur.x > 2*GAME_WIDTH/3:
                return True
            return False
        else:
            if self.pos_joueur.x < GAME_WIDTH/3:
                return True
            return False
    
    @property
    def replacement_gardien(self):
        if self.team == 1:
            return Vector2D(10, GAME_HEIGHT/2)
        else:
            return Vector2D(GAME_WIDTH - 10, GAME_HEIGHT/2)
            
    @property
    def replacement_def(self):
        if self.team == 1:
            return Vector2D(2*GAME_WIDTH/5, GAME_HEIGHT/2)
        else:
            return Vector2D(3*GAME_WIDTH/5, GAME_HEIGHT/2)

    @property
    def replacement_def4v4(self):
        if self.team == 1:
            return Vector2D(GAME_WIDTH/3, GAME_HEIGHT/2)
        else:
            return Vector2D(2*GAME_WIDTH/3, GAME_HEIGHT/2)

    @property
    def replacement_att2v2(self):
        if self.team == 1:
            return Vector2D(7*GAME_WIDTH/10, GAME_HEIGHT/2)
        else:
            return Vector2D(3*GAME_WIDTH/10, GAME_HEIGHT/2)

    @property
    def replacement_att4v4_haut(self):
        if self.team == 1:
            return Vector2D(6*GAME_WIDTH/10, 2*GAME_HEIGHT/3)
        else:
            return Vector2D(3*GAME_WIDTH/10, 2*GAME_HEIGHT/3)
        
    @property
    def replacement_att4v4_bas(self):
        if self.team == 1:
            return Vector2D(7*GAME_WIDTH/10, GAME_HEIGHT/3)
        else:
            return Vector2D(3*GAME_WIDTH/10, GAME_HEIGHT/3)

    @property
    #retourne la liste des opposant présents
    def near_opp(self):
        opponents = self.opponents_pos
        return min([self.pos_joueur.distance(player) for player in opponents])

    @property
    def near_opp2(self):
        return (self.near_opp, self.near_opp_ball)
    
    @property
    #retourne la distance entre la balle et son opposant le plus proche
    def near_opp_ball(self):
        opponents = self.opponents_pos
        opp_ball = [player.distance(self.pos_ball) for player in opponents]
        return min(opp_ball)

# Terrain
    @property
    def cage(self):
        return self.cage_def
    
    @property
    def cage_adv(self):
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2)
        else:
            return Vector2D(0, GAME_HEIGHT/2)
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
        if self.id_team == 1:
            return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
        else:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)

    @property
    def corner_haut_opp(self):
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT)
        else:
            return Vector2D(0, GAME_HEIGHT)

    @property
    def corner_bas_opp(self):
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH, 0)
        else:
            return Vector2D(0, 0)

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
        return Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)

