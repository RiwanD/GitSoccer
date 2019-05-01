
from socceria import
from soccersimulator import SoccerTeam

def get_team(nb_players):
	team = SoccerTeam(name="Nicolas&Riwan")
	if nb_payers == 1:
		team.add("CR7", uncontreun())
	if nb_payers == 2:
		team.add("CR7", attaquant())
		team.add("CR7", gardien())
	if nb_payers == 3:
		team.add("CR7", attaquant())
		team.add("CR7", gardien())
		team.add("CR7", libero())
	if nb_payers == 4:
		team.add("CR7", attaquantpointe())
		team.add("CR7", gardien())
		team.add("CR7", defenseur())
		team.add("CR7", libero())
	return team
#	
	
"""	if __name__ == '__main__':
		from soccersimulator import Simulation, show_simu
		
		team1 = get_team(1)
		team2 = get_team(2)
		
		simu = Simulation(team1, team2)
		
		show_simu(simu)
"""
