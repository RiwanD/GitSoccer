# -*- coding: utf-8 -*-

GAME_WIDTH = 150
GAME_HEIGHT = 90
GAME_GOAL_HEIGHT = 10
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65

#from . import settings
import soccersimulator
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from . import tools
from projet.tools import superstate

import projet.tools as to
import math, random

class Action(object):
    def __init__(self, name):
        self.name = name
    #def __getattr__(self, attr):
    #   return getattr(self.name, attr)
    #def computeAction(self, superstate):
    #   return soccersimulator.SoccerAction()
        
class Move(Action):
    def __init__(self, name):
        Action.__init__(self, name)


    def to_ball(self, to_ball):
            return soccersimulator.SoccerAction(acceleration = to.superstate.to_ball , shoot = None)
#Attaquant    
    def replacement_att_centre(self,replacement_att_centre):
        return soccersimulator.SoccerAction(acceleration = to.superstate.centre - superstate.position)

    def replacement_att_haut(self,replacement_att_haut):
        if to.superstate.team == 1:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.top_corner_right)/2  - superstate.position)
        else:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.top_corner_left)/2  - superstate.position)
    def replacement_att_bas(self,replacement_att_bas):
        if to.superstate.team == 1:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.bottom_corner_right)/2 - superstate.position)
        else:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.bottom_corner_left)/2  - superstate.position)
    def liste_replacements_att(self, replacements_att):
        replacements = [Move.replacement_att_haut, Move.replacement_att_centre, Move.replacement_att_bas]
        return replacements

    

    
#Defenseur
    def replacement_def_centre(self, replacement_def_centre):
        if to.superstate.team == 1:
            return soccersimulator.SoccerAction(acceleration = (GAME_WIDTH/3, GAME_HEIGHT/2) - superstate.position)

    def replacement_def_haut(self,replacement_def_haut):
        if to.superstate.team == 1:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.top_corner_left)/2  - superstate.position)
        else:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.top_corner_right)/2  - superstate.position)
    def replacement_def_bas(self,replacement_def_bas):
        if to.superstate.team == 1:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.bottom_corner_left)/2 - superstate.position)
        else:
            return soccersimulator.SoccerAction(acceleration = (to.superstate.centre -to.superstate.bottom_corner_right/2  - superstate.position))

    #Ici      
    def liste_replacements_def(self, replacements_def):
        replacements = [Move.replacement_def_haut, Move.replacement_def_centre, Move.replacement_def_bas]
        return replacements
        
    def def_Ramos(self,def_Ramos): 
        return soccersimulator.SoccerAction((to.superstate.ball - to.superstate.cage)/2, shoot = Vector2D.create_random())

    #Gardien
    def replacement_cage_centre(self, replacement_cage_centre):
        if to.superstate.team == 1:
            cage = soccersimulator.Vector2D(BALL_RADIUS + 2, GAME_HEIGHT/2)
            return soccersimulator.SoccerAction(cage - superstate.position, shoot = None)
        else:
            cage = soccersimulator.Vector2D(GAME_HEIGHT - BALL_RADIUS - 2, GAME_HEIGHT/2)
            return soccersimulator.SoccerAction(cage - superstate.position, shoot = None)
    
    def replacement_cage_haut(self,replacement_cage_haut):
        if to.superstate.team == 1:
                cage = soccersimulator.Vector2D(0+BALL_RADIUS, GAME_HEIGHT/2 + BALL_RADIUS + GAME_GOAL_HEIGHT/2)
                return soccersimulator.SoccerAction(cage - superstate.position, shoot = None)
        else:
            cage = soccersimulator.Vector2D(GAME_WIDTH + BALL_RADIUS, GAME_HEIGHT/2 + BALL_RADIUS + GAME_GOAL_HEIGHT/2 )
            return soccersimulator.SoccerAction(cage - superstate.position, shoot = None)
    
    def replacement_cage_bas(self,replacement_cage_bas):
        if to.superstate.team == 1:
                cage = soccersimulator.Vector2D(0+BALL_RADIUS,GAME_HEIGHT/2 - BALL_RADIUS - GAME_GOAL_HEIGHT/2)
                return soccersimulator.SoccerAction(cage - superstate.position, shoot = None)
        else:
            cage = soccersimulator.Vector2D(GAME_HEIGHT -BALL_RADIUS,GAME_HEIGHT/2 - BALL_RADIUS - GAME_GOAL_HEIGHT/2)
            return soccersimulator.SoccerAction(cage - superstate.position, shoot = None)
    
    def liste_replacements_cage(self, replacements_cage):
        replacements = [Move.replacement_cage_haut, Move.replacement_cage_centre, Move.replacement_cage_bas]
        return replacements
            
class Shoot(Action):
    def __init__(self, name):
        Action.__init__(self, name)

    def to_goal(self):
        return soccersimulator.SoccerAction(acceleration=None, shoot = to.superstate.cage_adv)
    
    def shoot_poss(self, shoot_off):
        opp = to.superstate.opponents_rect
        l_vide = []
        if opp != l_vide:
            return soccersimulator.SoccerAction(Vector2D.create_random(), Vector2D.create_random())
        else:
            return soccersimulator.SoccerAction(acceleration = None, shoot = Shoot.to_goal)

    
    



"""
class Gardien(Move):
    def __init__(self):
        Move.__init__(self, "Gardien")
    def computeAction(self, superstate):
        if (dist < PLAYER_RADIUS + BALL_RADIUS):
            return Move.To_ball()
        if self.player.player_state(self.id_team) == 1:
            if ((superstate.ball.y >= (2*GAME_HEIGHT)/3) and (superstate.ball.x <=GAME_WIDTH/3)):
                def = soccersimulator.Vector2D(0+BALL_RADIUS, GAME_HEIGHT/2 + BALL_RADIUS + GAME_GOAL_HEIGHT/2)
                return soccersimulator.SoccerAction(def - superstate.position, shoot = None)
            if ((superstate.ball.y < GAME_HEIGHT/3) and (superstate.ball.x <= GAME_WIDTH/3)):
                def = soccersimulator.Vector2D(0+BALL_RADIUS,GAME_HEIGHT/2 - BALL_RADIUS - GAME_GOAL_HEIGHT/2)
                return soccersimulator.SoccerAction(def - superstate.position, shoot = None)
            if ((superstate.ball.y > GAME_HEIGHT/3) and (superstate.ball.y < (2*GAME_HEIGHT)/3) and (superstate.ball.x <=GAME_WIDTH/3)):
                def = soccersimulator.Vector2D(BALL_RADIUS + 2, GAME_HEIGHT/2)
                return soccersimulator.SoccerAction(def - superstate.position, shoot = None)
        if self.player.player_state(self.id_team) == 2:
            if ((superstate.ball.y >= (2*GAME_HEIGHT)/3) and (superstate.ball.x >=2*GAME_WIDTH/3) ):
                def = soccersimulator.Vector2D(GAME_WIDTH + BALL_RADIUS, GAME_HEIGHT/2 + BALL_RADIUS + GAME_GOAL_HEIGHT/2 )
                return soccersimulator.SoccerAction(def - superstate.position, shoot = None)
            if ((superstate.ball.y < GAME_HEIGHT/3) and (superstate.ball.x >= 2*GAME_WIDTH/3)):
                def = soccersimulator.Vector2D(GAME_HEIGHT -BALL_RADIUS,GAME_HEIGHT/2 - BALL_RADIUS - GAME_GOAL_HEIGHT/2)
                return soccersimulator.SoccerAction(def - superstate.position, shoot = None)
            if ((superstate.ball.y > GAME_HEIGHT/3) and (superstate.ball.y < (2*GAME_HEIGHT)/3) and (superstate.ball.x >=2*GAME_WIDTH/3)):
                def = soccersimulator.Vector2D(GAME_HEIGHT - BALL_RADIUS - 2, GAME_HEIGHT/2)
                return soccersimulator.SoccerAction(def - superstate.position, shoot = None)
    """    

#Seul

"""                  
class passe(object):
    def __init__(self, superstate):
        self.superstate = superstate

    def passe(self, direction= None):
        dist = self.superstate.player.distance(self.superstate.ball)
        n1 = superstate.near_opp
        if dist  < PLAYER_RADIUS + BALL_RADIUS:
             return SoccerAction(shoot=direction)
        else:
             return SoccerAction()
"""
