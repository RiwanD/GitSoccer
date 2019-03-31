from superstate import SuperState

class Opponent(Strategy):
	def __init__(self, vitesse, position, action, name="opposition"):
		super().__init__(name)
		self.position = position
		self.vitesse = vitesse
		
	def att_ou_def(self, state, id_team, id_player):
		s = SuperState(state, id_team, id_player)
		if 
		
		
