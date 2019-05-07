# -*- coding: utf-8 -*-

GAME_WIDTH = 150
GAME_HEIGHT = 90
GAME_GOAL_HEIGHT = 10
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
maxPlayerShoot = 6.
#from . import settings
import soccersimulator
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIUS
from . import tools
from .tools import superstate
from . import utils
from soccersimulator.utils import random

import projet.tools as to

import math, random

class Action(object):
    def __init__(self, name="action"):
        self.name = name
    #def __getattr__(self, attr):
    #   return getattr(self.name, attr)
    #def computeAction(self, superstate):
    #   return soccersimulator.SoccerAction()
        
class Move(Action):
    def __init__(self, name=None):
        if name is not None:
            super(Move, self).__init__(name)
        else:
            super(Move, self).__init__()

#Attaquant    
    def replacement_att(self, pos_joueur, replacement_att):
        return soccersimulator.SoccerAction(acceleration = replacement_att - pos_joueur)

    """
    def liste_replacements_att(self, replacements_att):
        replacements = [self.replacement_att_haut, self.replacement_att_centre, self.replacement_att_bas]
        return replacements
    """
    
    def to_ball(self, pos_ball, pos_player):
        ball = pos_ball
        player = pos_player
        return soccersimulator.SoccerAction(acceleration = ball - player , shoot = None)

    def appel(self, pos_joueur, pos_appel):
        return soccersimulator.SoccerAction(acceleration= pos_appel - pos_joueur, shoot = None)
    
#Defenseur

    def replacement_def(self, pos_joueur, replacement_def):
        return soccersimulator.SoccerAction(acceleration = replacement_def - pos_joueur)
       
    def def_Ramos(self, pos_joueur, pos_ball, pos_cage, vect_vitesse_joueur):
        vect_ball_cage = pos_ball - pos_cage
        expected_pos = vect_ball_cage/2 + pos_cage #changement d'origine car vect_ball_cage est à y = 0
        vect_move = utils.compute_move(pos_joueur, vect_vitesse_joueur, expected_pos)
        action = soccersimulator.SoccerAction(acceleration = vect_move, shoot = None)
        return action

    def joueur_vers_ball(self, pos_joueur, pos_ball, vect_vitesse_joueur):
        vect_joueur_ball = pos_ball - pos_joueur
        #expected_pos =  pos_ball
        #vect_move = utils.compute_move(pos_joueur, vect_vitesse_joueur, expected_pos)
        return soccersimulator.SoccerAction(acceleration = vect_joueur_ball, shoot = None)

    def joueur_entre_adv(self, pos_joueur, opp, next_opp):
        expected_pos = (opp - next_opp)/2 + opp
        vect_joueur_entre_opp = expected_pos - pos_joueur
        return soccersimulator.SoccerAction(acceleration = vect_joueur_entre_opp, shoot = None)
    #Gardien
    def replacement_cage_centre(self, pos_joueur, replacement_gardien):
        if tools.superstate.team == 1:
            return soccersimulator.SoccerAction(acceleration = replacement_gardien - pos_joueur, shoot = None)
    """
    def pos_gardien_attente(self, pos_joueur, pos_ball, pos_cage, vect_vitesse_joueur):
        vect_ball_cage = pos_ball - pos_cage
        expected_pos = vect_ball_cage/15 + pos_cage #changement d'origine car vect_ball_cage est à y = 0
        pass
    """
    def DeGea_pos(self, pos_joueur, pos_ball, pos_cage, vect_vitesse_joueur):
        vect_ball_cage = pos_ball - pos_cage
        expected_pos = vect_ball_cage/7 + pos_cage #changement d'origine car vect_ball_cage est à y = 0
        vect_move_norm = utils.compute_move(pos_joueur, vect_vitesse_joueur, expected_pos)
        vect_move = expected_pos - pos_joueur
        action = soccersimulator.SoccerAction(acceleration = vect_move, shoot = None)
        return action
class Shoot(Action):
    def __init__(self, name=None):
        if name is not None:
            super(Shoot, self).__init__(name)
        else:
            super(Shoot, self).__init__()

    def to_goal(self, pos_ball, pos_player,cage_adv, strength):
        vect = cage_adv - pos_player
        vect.normalize()
        return soccersimulator.SoccerAction(acceleration = None , shoot = vect * strength)

    def goal_shoot(self,pos_joueur, pos_cage_adv, puissance_tir):
        aimed_pos = pos_cage_adv
        tir = utils.compute_shoot(aimed_pos, pos_joueur, puissance_tir)
        vect_tir = (aimed_pos - pos_joueur) 
        return soccersimulator.SoccerAction(acceleration=None, shoot = vect_tir)

    def avancer_avec_ball(self, pos_joueur, pos_cage_adv, puissance_tir):
        aimed_pos = pos_cage_adv
        tir = utils.compute_shoot(aimed_pos, pos_joueur, puissance_tir)
        return soccersimulator.SoccerAction(acceleration=None, shoot = tir)

    def shoot_aim(self,pos_joueur, aimed_pos, puissance_tir):
        tir = utils.compute_shoot(aimed_pos, pos_joueur, puissance_tir)
        vect_tir = (aimed_pos - pos_joueur)
        return soccersimulator.SoccerAction(acceleration=None, shoot = vect_tir)

    def puissance_tir(self, p_tir):
        return p_tir
    
        #retourne la liste des opposant présents dans le rectangle défini entre le joueur et les cages adverses 
    
    """
    def shoot_poss(self, expected_pos):
        opp = tools.superstate.opponents_rect
        l_vide = []
        pos_ball = tools.superstate.pos_ball
        pos_cage_adv = tools.superstate.cage_adv
        puissance_shoot = self.puissance_tir(6)

        if opp == l_vide:
            return True
        else:
            return False
    """
    def degagement(self):
        aimed_pos = random.random()*(40) + 40
        random_pos= random.random()*10
        if tools.superstate.team == 1:
            #return soccersimulator.SoccerAction( acceleration = None, shoot = Vector2D( random.random()*10 , aimed_pos - 80))
            return soccersimulator.SoccerAction( acceleration = None, shoot = Vector2D(GAME_WIDTH, random_pos))
        else:
            #return soccersimulator.SoccerAction( acceleration = None, shoot = Vector2D( random.random()*10, aimed_pos))
            return soccersimulator.SoccerAction( acceleration = None, shoot = Vector2D( random_pos -100, random_pos))

    def passe(self, pos_joueur, pos_ball, pos_mate, aimed_pos, shoot_poss, pos_cage_adv):
        puissance_tir = 6
        #Si il y a des equipiers et que le shoot est impossible 
        if not shoot_poss:
        #if tools.superstate.team == 1:
            #if pos_joueur.x < 2*GAME_HEIGHT/3 :
                #il fait la passe
            return self.shoot_aim(pos_joueur, pos_mate, puissance_tir)
        else:
            shoot = utils.compute_shoot(pos_joueur, pos_cage_adv,puissance_tir)
            return soccersimulator.SoccerAction(acceleration = None, shoot = shoot)


    def passe2(self, pos_joueur, pos_mate, puissance_tir):
        return self.shoot_aim(pos_joueur, pos_mate, puissance_tir)

   
    """    
    def shoot_poss(self, pos_joueur, aimed_pos):
        joueurs_all = tools.superstate.pos_joueurs_all(tools.superstate)
        opp = [tools.superstate.state.player_state(id_team, id_player).position for (id_team, id_player) in joueurs_all if id_team != tools.superstate.team]
        if tools.superstate.team == 1:
            opp_f =[tools.superstate.state.player_state(id_team, id_player).position for (id_team, id_player) in opp 
            if tools.superstate.state.player_state(id_team, id_player).position.x > tools.superstate.pos_joueur.x]
            contreurs_pot = [tools.superstate.state.player_state(id_team, id_player).position for (id_team, id_player) in opp_f]
        else:
            opp_f = [tools.superstate.state.player_state(id_team, id_player).position for (id_team, id_player) in opp 
            if tools.superstate.state.player_state(id_team, id_player).position.x < tools.superstate.pos_joueur.x]
            contreurs_pot = [tools.superstate.state.player_state(id_team, id_player).position for (id_team, id_player) in opp_f]

        vect_exp_shoot = aimed_pos - pos_joueur
        dist_exp_shoot_norm = vect_exp_shoot.normalize()
        dist_joueur_contreurs = [pos_joueur.distance(player) for player in contreurs_pot]
        dist_aimed_pos_contreur = [aimed_pos.distance(player) for player in contreurs_pot]
        dist_totale = dist_joueur_contreurs + dist_aimed_pos_contreur
        if dist_exp_shoot_norm*1.3 >= dist_totale:
            return True
        else:
            return False
    """