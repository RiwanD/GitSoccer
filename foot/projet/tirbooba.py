from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet.tools import superstate
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-1,1),
                            Vector2D.create_random(-1,1))



class booba(Strategy):
    def __init__(self):
        Strategy.__init__(self, "booba")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        teta = -(state.player_state(1,0).position.x)*(state.ball.position.x)+(state.player_state(1,0).position.y)*(state.ball.position.y)
        angle = (state.player_state(1,0).position.x - 150), (state.player_state(1,0).position.y)
        if id_team == 1:
            return SoccerAction(state.ball.position-state.player_state(1, 0).position,
                   state.ball.position-state.player_state(1 ,0).position * teta)
        else:
            return SoccerAction(state.ball.position-state.player_state(2, 0).position,
                   state.ball.position-state.player_state(2 ,0).position * teta)
   # 
    def Defenseur(Strategy):
        def __init__(self):
            Strategy.__init__(self,"Def")

        def compute_strategy(self, state, id_team, id_player):
                return SoccerAction((superstate.ball - superstate.cage)/2, shoot = None)
        
    def shoot(self, direction=None):
        if dist < PLAYER_RADIUS + BALL_RADIUS:
            return SoccerAction(state.ball.position-state.player_state(1 ,0).position)
        else:
            return SoccerAction()


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("booba", booba())
team2.add("Ramos", Defenseur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
  
