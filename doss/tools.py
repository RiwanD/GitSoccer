from soccersimulator import settings, utils, strategies, events, mdpsoccer, matches
import math






class superstate(object):
	def __init__(self,state,id_team,id_player):
		self.state=state
		self.id_team=id_team
		self.id_player=id_player
		
		
		
		#La Balle
		@property
		def ball(self):
			return self.state.ball.position
		
		@property
		def distanceBal(self):
			return self.superstate.player.distance(self.superstate.ball)
			
		#Joueur
		@property
		def team(self):
			return self.state.player_state(seld.id_team)
		
		@property
		def position(self):
			return self.state.player_state(self.id_team,self.id_player).position
			
		@property
		def player(self):
			return self.state.player_state(self.id_team,self.id_player)
			
		@property
		def vitesse(self):
			return self.player.vitesse
			
		@property
		def to_Ball(self):
			return Vector2D(self.ball.x -self.position.x,self.ball.y-self.position.y)
			
			
		#Equipier
		
		@property
		def mate(self):
			return [self.state.player_state(id_team,id_player).position for (id_team,id_player) in self.state.players if id_team == self.id_team]
			
			@property
			def near_mate(self):
				mate=self.mate
				return min([(self.player.position.distance(player),player) for player in mate])
			
			@property
			def near_mate_ball(self):
				mate=self.mate
				return min([self.player.playerstate(self.ball) for player in mate])
			
			
		#Ennemi
		@property
		def opp(self):
			return [self.state.player_state(id_team,id_player).position for (id_team,id_player) in self.state.players if id_team != self.id_team]
		
			@property
			def near_opp(self):
				opp=self.opp
				return min([(self.player.position.distance(player),player) for player in opp])
			
			@property
			def near_opp_ball(self):
				opp=self.opp
				return [self.state.playerstate(self.ball) for player in opp]		


		#terrain
		@property
		def cageequipe1(self):
			return Vector2D(0,GAME_HEIGHT/2 +5)
			
		@property
		def cage2equipe1(self):
			return Vector2D(0,GAME_HEIGHT/2-5)
				
		@property
		def cageequipe2(self):
			return Vector2D(GAME_WIDTH,GAME_HEIGHT/2+5)
			
		@property
		def cage2equipe2(self):
			return Vector2D(GAME_WIDTH,GAME_HEIGHT/2-5)
			
		@property
		def centre(self):
			return Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)
			
			
			
		
		
