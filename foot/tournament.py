# coding: utf-8

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet.actions import Action, Move, Shoot
from projet.tools import superstate
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIUS
from strategies import Gardien, Def2v2, Attaquant2v2, Attaquant4v4, Def4v4, Milieu
def get_team(nb_players):
	team = SoccerTeam(name="Riwan")
	if nb_players == 1:
		team.add("CR7", AttDef())
	if nb_players == 2:
		team.add("CR7", Attaquant2v2())
		team.add("DeGea", Def2v2())

	if nb_players == 4:
		team.add("Gardien", Gardien())
		team.add("Def", Def4v4())
		team.add("Mil", Milieu())
		team.add("Att", Attaquant4v4())
	return team
#	
	
if __name__ == '__main__':

		team1 = get_team(4)
		team2 = get_team(4)
		
		simu = Simulation(team1, team2)
		
		show_simu(simu)
