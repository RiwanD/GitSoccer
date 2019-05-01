from soccersimulator import setting, utils, stategies, events, mdpsoccer, matches, superstate, tools
from tools import *
import soccersimlator as so
import tools as to

class DefenseStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self, "Defense")
		
	def compute_strategy(self, state, id_team, id_player):
		s = SuperState(state, id_team, id_player)
		if (superstate.ball.x < GAME_WIDTH/2):
			move = Move(s)
			shoot = Shoot(s)
			return move + shoot
#