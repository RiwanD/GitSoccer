# coding: utf-8

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet.actions import Action, Move, Shoot
from projet.tools import superstate
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIUS
from . import Gardien

def get_team(nb_players):
	team = SoccerTeam(name="Nicolas&Riwan")
	if nb_payers == 1:
		team.add("CR7", AttDef())
	if nb_payers == 2:
		team1.add("CR7", Attaquant2v2())
		team1.add("DeGea", Def())
		team2.add("Messi", Attaquant2v2())
		team2.add("Lloris", Def())

	if nb_payers == 4:
		team.add("CR7", Gardien())
		team.add("CR7", Def())
		team.add("CR7", Milieu())
		team.add("CR7", Attaquant())
		team.add("CR7", Gardien())
		team.add("CR7", Def())
		team.add("CR7", Milieu())
		team.add("CR7", Attaquant())
	return team
#	
	
if __name__ == '__main__':

		team1 = get_team(1)
		team2 = get_team(2)
		
		simu = Simulation(team1, team2)
		
		show_simu(simu)
