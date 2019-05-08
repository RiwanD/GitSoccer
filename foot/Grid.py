from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet.actions import Action, Move, Shoot
from projet.tools import superstate
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIUS, GAME_HEIGHT, GAME_WIDTH
from sklearn.model_selection import ParameterGrid


class GoalSearch (object):
    def __init__(self, strategy, strategy2, params, simu = None, trials = 10,
                  max_steps = 1000000, max_round_step = 45):
        self.strategy = strategy
        self.strategy2 = strategy2
        self.params = params.copy()
        self.simu = simu
        self.trials = trials
        self.max_steps = max_steps
        self.max_round_step = max_round_step
    
    def start(self , show = True):
        if not self.simu :
            team1 = SoccerTeam(" Team ␣ 1 ")
            team2 = SoccerTeam (" Team ␣ 2 ")
            team1.add(self.strategy.name, self.strategy)
            team1.add(self.strategy2.name, self.strategy2)
            team2.add(Strategy().name, Strategy())
            self.simu = Simulation (team1, team2, max_steps = self.max_steps)
        self.simu.listeners += self
        
        if show:
            show_simu(self.simu )
        else:
            self.simu.start()

    def begin_match(self, team1, team2, state):
        self.last_step = 0 # Step of the last round
        self.criterion = 0 # Criterion to maximize ( here , number of goals )
        self.cpt_trials = 0 # Counter for trials
        self.param_grid = iter(ParameterGrid(self.params)) # Iterator for the g
        self.cur_param = next(self.param_grid , None) # Current parameter
        if self.cur_param is None:
            raise ValueError('no parameter given.')
        self.res = dict() # Dictionary of results
    
    def begin_round(self, team1, team2, state):
        ball = Vector2D.create_random(low =0 , high =1)
        ball.x += 75
        ball.y += GAME_HEIGHT/2
        
        # Player and ball postion ( random )
        self.simu.state.states[(1, 0)].position = ball.copy() # Player position
        self.simu.state.states[(1, 0)].vitesse = Vector2D() # Player accelerati
        self.simu.state.ball.position = ball.copy() # Ball position
        self.last_step = self.simu.step  # Last step of the game

        self.simu.state.states[(1, 1)].position = Vector2D(3*GAME_WIDTH/4, GAME_WIDTH/2) # Player position
        self.simu.state.states[(1, 1)].vitesse = Vector2D() # Player accelerati
        
        # Set the current value for the current parameters
        for key, value in self.cur_param.items():
            setattr(self.strategy, key, value)
            
    def end_round(self , team1 , team2 , state):
        # A round ends when there is a goal of if max step is achieved
        #if state.goal > 0:
        if self.simu.state.states[(1, 1)].position != Vector2D(3*GAME_WIDTH/4, GAME_WIDTH/2):
            self.criterion += 1 # Increment criterion
        
        self.cpt_trials += 1 # Increment number of trials
        
        print(self.cur_param)
        print(" Crit : ␣{}␣␣␣ Cpt :␣{} ". format(self.criterion, self.cpt_trials))

        if self.cpt_trials >= self.trials :
            # Save the result
            self.res[tuple(self.cur_param.items())] = self.criterion * 1./self.trials

            # Reset parameters
            self.criterion = 0
            self.cpt_trials = 0

            # Next parameter value
            self.cur_param = next(self.param_grid, None)
            if self.cur_param is None :
                self.simu.end_match()
                
    def update_round (self, team1, team2, state):
        # Stop the round if it is too long
        if state.step > self.last_step + self.max_round_step:
            self.simu.end_round()
            
    def get_res(self):
        return self.res
    
    def get_best(self):
        return max(self.res, key = self.res.get)
    
class GoTestStrategy(Strategy):
    def __init__(self, strength=None):
        Strategy.__init__(self, "Go-getter")
        self.strength = strength
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_joueur = s.pos_joueur
        cage_adv = s.cage_adv
        pos_ball = s.pos_ball
        return move.to_ball(pos_ball, pos_joueur) + shoot.to_goal(pos_ball, pos_joueur,cage_adv,self.strength)

class GoTestStrategy2(Strategy):
    def __init__(self, strength=None):
        Strategy.__init__(self, "Go-getter")
        self.strength = strength
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_joueur = s.pos_joueur
        cage_adv = s.cage_adv
        pos_ball = s.pos_ball
        pos_mate = s.mate_front[0]
        return  shoot.passe2(pos_joueur, pos_mate, self.strength)


