
from soccersimulator import setting, utils, strategies, events, mdpsoccer, matches, superstate, tools
from tools import *
import soccersimulator as so
import tools as to


class Action:
	def __init__(self, name):
		self.name = name
	def computeAction(self, superstate):
		return so.SoccerAction()
		
class Move(Action):
    def __init__(self, name):
        Action.__init__(self, name)

class Shoot(Action):
    def __init__(self, name):
        Action.__init__(self, name)
        


class To_ball(Move):
		def __init__(self):
			Move.__init__(self, "To_ball")
		def computeAction(self, superstate):
				return so.SoccerAction(acceleration = superstate.ball - superstate.position)


class retraitstrat(move):
        def __init__(self):
            Move.__init__(self,"retraitstrat")
        def computeAction(self,superstate):
            return so.SoccerAction(acceleration=superstate.near_mate)

                    
                    
class Attaquant(self):
    def __init__(self):
        Move.__init__(self,"Attaquant")
    def computeAction(self,superstate):
        if self.id_team == 1:
            if (compteurball1>compteurball2):
                return Move.To_ball()
            else:
                return
    
    
    
#En defense


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
        n1 = near_opp
        if dist  < PLAYER_RADIUS + BALL_RADIUS:
             return SoccerAction(shoot=direction)
        else:
             return SoccerAction()

#En equipe
        
    def near_opp(self):
        opp = [self.state.player(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
        
        return min([(self.player.disctance(player), player) for player in opp])[1]
    
 #type de défenseur
 
   
class gardien(self):
    def init(self):
        Move.init(self, "Gardien")
    def computeAction(self, superstate):
        if self.player.player_state(self.id_team) == 1:
            if ((superstate.ball.y >= (2*GAME_HEIGHT)/3) and (superstate.ball.x <=GAME_WIDTH/3)):
                cage = so.Vector2D(0+BALL_RADIUS, GAME_HEIGHT/2 + BALL_RADIUS + GAME_GOAL_HEIGHT/2)
                return so.SoccerAction(cage - superstate.position, shoot = None)
            elif ((superstate.ball.y < GAME_HEIGHT/3) and (superstate.ball.x <= GAME_WIDTH/3)):
                cage = so.Vector2D(0+BALL_RADIUS,GAME_HEIGHT/2 - BALL_RADIUS - GAME_GOAL_HEIGHT/2)
                return so.SoccerAction(cage - superstate.position, shoot = None)
            elif ((superstate.ball.y > GAME_HEIGHT/3) and (superstate.ball.y < (2*GAME_HEIGHT)/3) and (superstate.ball.x <=GAME_WIDTH/3)):
                cage = so.Vector2D(BALL_RADIUS + 2, GAME_HEIGHT/2)
                return so.SoccerAction(cage - superstate.position, shoot = None)
		if self.player.player_state(self.id_team) == 2:
			if ((superstate.ball.y >= (2*GAME_HEIGHT)/3) and (superstate.ball.x >=2*GAME_WIDTH/3)):
				cage = so.Vector2D(GAME_WIDTH + BALL_RADIUS, GAME_HEIGHT/2 + BALL_RADIUS + GAME_GOAL_HEIGHT/2 )
				return so.SoccerAction(cage - superstate.position, shoot = None)
            if ((superstate.ball.y < GAME_HEIGHT/3) and (superstate.ball.x >= 2*GAME_WIDTH/3)):
                cage = so.Vector2D(GAME_HEIGHT -BALL_RADIUS,GAME_HEIGHT/2 - BALL_RADIUS - GAME_GOAL_HEIGHT/2)
                return so.SoccerAction(cage - superstate.position, shoot = None)
            if ((superstate.ball.y > GAME_HEIGHT/3) and (superstate.ball.y < (2*GAME_HEIGHT)/3) and (superstate.ball.x >=2*GAME_WIDTH/3)):
                cage = so.Vector2D(GAME_HEIGHT - BALL_RADIUS - 2, GAME_HEIGHT/2)
                return so.SoccerAction(cage - superstate.position, shoot = None)
