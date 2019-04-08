
from soccersimulator import strategies, settings



class Superstate(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_player = id_player
        self.id_team = id_team
    
    # Balle
    @property
    def ball(self):
        return self.state.ball.position
    @property
    def dist(self):
        return self.superstate.player.distance(self.superstate.ball)
        
        @property
        def trajectoire(self):
            return Vector2D(cage_adv_x - position.x, cage_adv_y - position.y)
   
    def compteurball1(self):
        return compteurball1
    
    def compteurball2(self):
        return compteurball2

    def possession(self):
        
        if(near_mate_ball>near_opp_ball):
            return self.compteurball1+1
        if(near_mate_ball!=near_opp_ball):
            pass
        else:
            return self.compteurball2+1

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
        #def shoot_possible(self):
           # if Vector2D
        
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
        
        @property
        def cage_adv_x(self):
            return self.cage_adv()[1]
        
        @property
        def cage_adv_y(self):
            return self.cage_adv()[2]
        #@property
        #def cage_def(self):
		#	if self.state.player_state(self.id_team) ==1:
		#		return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
		#	else:
			#	return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)
                
