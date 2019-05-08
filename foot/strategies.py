# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from projet.actions import Action, Move, Shoot
from projet.tools import superstate
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIUS
GAME_WIDTH = 150
GAME_HEIGHT = 90
GAME_GOAL_HEIGHT = 10

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(),
                            Vector2D.create_random())
#
"""class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")

    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball(superstate.to_ball) + shoot.to_goal()
"""

class Attaquant2v2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_ball = s.pos_ball
        cage_adv = s.cage_adv
        pos_joueur = s.pos_joueur
        pos_appel_de_ball = s.appel_de_balle
        vect_vitesse_joueur = s.vitesse_joueur
        replacement = s.replacement_att2v2
        #puissance_tir = shoot.puissance_tir(0.1)
        approxi_pos_ball = s.approxi_pos_ball
        puissance_tir = 6
        near_opp_ball = s.near_opp_ball
        near_mate_ball = s.near_mate_ball
        dist_joueur_ball = s.dist_joueur_ball
        if s.team == 1:
            #si la balle est dans le camp adverse
            if(approxi_pos_ball.x >= GAME_WIDTH/2):
                mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                tir = shoot.goal_shoot(pos_joueur, cage_adv, puissance_tir)
                action = mouvement + tir
                return action
            else:
                #si un coequipier peut avoir la balle il fait un appel 
                if (near_mate_ball < near_opp_ball):
                    mouvement = move.appel(pos_joueur, pos_appel_de_ball)
                    return mouvement
                #sinon il se replace
                else:
                    #S'il est seul il dézone pour tirer
                    if (approxi_pos_ball.x >= GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                        mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                        passe = shoot.avancer_avec_ball(pos_joueur, cage_adv, puissance_tir)
                        return mouvement + passe
                    #sinon il se replace
                    else:
                        mouvement = move.replacement_att(pos_joueur, replacement)
                        return mouvement
        else:
            #si la balle est dans le camp adverse
            if(approxi_pos_ball.x <= GAME_WIDTH/2):
                mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                tir = shoot.goal_shoot(pos_joueur, cage_adv, puissance_tir)
                action = mouvement + tir
                return action
            else:
                #si un coequipier peut avoir la balle il fait un appel 
                if (near_mate_ball < near_opp_ball):
                    mouvement = move.appel(pos_joueur, pos_appel_de_ball)
                    return mouvement
                else:
                    #S'il est seul il dézone pou faire une passe
                    if (approxi_pos_ball.x >= 2*GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                        mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                        passe = shoot.avancer_avec_ball(pos_joueur, cage_adv, puissance_tir)
                        return mouvement + passe
                    #sinon il se replace
                    else:
                        mouvement = move.replacement_att(pos_joueur, replacement)
                        return mouvement

class Def2v2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_joueur = s.pos_joueur
        pos_ball = s.pos_ball
        pos_cage = s.cage_def
        cage_adv = s.cage_adv
        replacement_def = s.replacement_def
        corner_haut_opp = s.corner_haut_opp
        vect_vitesse_joueur = s.vitesse_joueur
        approxi_pos_ball = s.approxi_pos_ball
        dist_joueur_ball = s.dist_joueur_ball
        near_opp_ball = s.near_opp_ball
        action = move.def_Ramos(pos_joueur, pos_ball, pos_cage, vect_vitesse_joueur)
        near_mate = s.mate_front[0]
        pos_opp = s.opponents_pos
        shoot_poss = s.shoot_poss(pos_joueur, near_mate)
        puissance_tir = 6
        
        if s.team == 1:
            #si elle est dans son camp:
            if(approxi_pos_ball.x <= GAME_WIDTH/2):
                #il se met en place pour l'intercepter et fait la passe à l'attaquant
                approxi_pos_ball = s.pos_ball + 6*s.vitesse_ball
                if dist_joueur_ball <= near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else: 
                    defense = move.DeGea_pos(pos_joueur, approxi_pos_ball, pos_cage, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return defense + passe
            #sinon il se replace
            else:
                #S'il est seul il dézone pou faire une passe
                if (approxi_pos_ball.x <= 2*GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else:
                    defense = move.replacement_def(pos_joueur, replacement_def)
                    return defense       
        if s.team == 2:
            #si elle est dans son camp:
            if(approxi_pos_ball.x >= GAME_WIDTH/2):
                #il se met en place pour l'intercepter et fait la passe à l'attaquant
                if dist_joueur_ball <= near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else: 
                    defense = move.DeGea_pos(pos_joueur, approxi_pos_ball, pos_cage, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return defense + passe
            #sinon il se replace
            else:
                #S'il est seul il dézone pou faire une passe
                if (approxi_pos_ball.x >= GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else:
                    defense = move.replacement_def(pos_joueur, replacement_def)
                    return defense      


class Attaquant4v4(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_ball = s.pos_ball
        cage_adv = s.cage_adv
        pos_joueur = s.pos_joueur
        pos_appel_de_ball = s.appel_de_balle
        vect_vitesse_joueur = s.vitesse_joueur
        replacement = s.replacement_att4v4_haut
        #puissance_tir = shoot.puissance_tir(0.1)
        approxi_pos_ball = s.approxi_pos_ball
        puissance_tir = 6
        near_opp_ball = s.near_opp_ball
        near_mate_ball = s.near_mate_ball
        dist_joueur_ball = s.dist_joueur_ball
        if s.team == 1:
            #si la balle est dans le camp adverse
            if(approxi_pos_ball.x >= GAME_WIDTH/2):
                #Et qu'un allier a la balle: 
                if near_mate_ball < near_opp_ball:
                    mouvement = move.appel(pos_joueur, pos_appel_de_ball)
                    tir = shoot.goal_shoot(pos_joueur, cage_adv, puissance_tir)
                    action = mouvement + tir
                    return action
                else:
                    #Sinon il va tirer
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    tir = shoot.goal_shoot(pos_joueur, cage_adv, puissance_tir)
                    action = mouvement + tir
                    return action
            else:
                #si un coequipier peut avoir la balle il fait un appel 
                if (near_mate_ball < near_opp_ball):
                    mouvement = move.appel(pos_joueur, pos_appel_de_ball)
                    return mouvement
                #sinon il se replace
                else:
                    #S'il est seul il dézone pour tirer
                    if (approxi_pos_ball.x >= GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                        mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                        passe = shoot.avancer_avec_ball(pos_joueur, cage_adv, puissance_tir)
                        return mouvement + passe
                    #sinon il se replace
                    else:
                        mouvement = move.replacement_att(pos_joueur, replacement)
                        return mouvement
        else:
            #si la balle est dans le camp adverse
            if(approxi_pos_ball.x <= GAME_WIDTH/2):
                #Et qu'un allier a la balle: 
                if near_mate_ball < near_opp_ball:
                    mouvement = move.appel(pos_joueur, pos_appel_de_ball)
                    tir = shoot.goal_shoot(pos_joueur, cage_adv, puissance_tir)
                    action = mouvement + tir
                    return action
                else:
                    #Sinon il va tirer
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    tir = shoot.goal_shoot(pos_joueur, cage_adv, puissance_tir)
                    action = mouvement + tir
                    return action
            else:
                #si un coequipier peut avoir la balle il fait un appel 
                if (near_mate_ball < near_opp_ball):
                    mouvement = move.appel(pos_joueur, pos_appel_de_ball)
                    return mouvement
                else:
                    #S'il est seul il dézone pou faire une passe
                    if (approxi_pos_ball.x >= 2*GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                        mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                        passe = shoot.avancer_avec_ball(pos_joueur, cage_adv, puissance_tir)
                        return mouvement + passe
                    #sinon il se replace
                    else:
                        mouvement = move.replacement_att(pos_joueur, replacement)
                        return mouvement


class Def4v4(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_joueur = s.pos_joueur
        pos_ball = s.pos_ball
        pos_cage = s.cage_def
        cage_adv = s.cage_adv
        replacement_def = s.replacement_def4v4
        corner_haut_opp = s.corner_haut_opp
        vect_vitesse_joueur = s.vitesse_joueur
        approxi_pos_ball = s.approxi_pos_ball
        dist_joueur_ball = s.dist_joueur_ball
        near_opp_ball = s.near_opp_ball
        action = move.def_Ramos(pos_joueur, pos_ball, pos_cage, vect_vitesse_joueur)
        near_mate = s.mate_front[0]
        near_ball_mate = s.near_mate_ball
        pos_opp = s.opponents_pos
        shoot_poss = s.shoot_poss(pos_joueur, near_mate)
        appel_def = s.replacement_def4v4
        puissance_tir = 6
        mate_front = s.mate_front[0]
        
        if s.team == 1:
            #si elle est dans son camp:
            if(approxi_pos_ball.x <= GAME_WIDTH/2):
                #il se met en place pour l'intercepter et fait la passe à l'attaquant
                approxi_pos_ball = s.pos_ball + 6*s.vitesse_ball
                #Si elle est dans la zone du gardien 
                if approxi_pos_ball.x < GAME_WIDTH/5:
                    #Et qu'il a la balle
                    if  near_ball_mate <= near_opp_ball:
                        mouvement = move.appel(pos_joueur, appel_def)
                        return mouvement
                    #sinon il fonce vers la balle et tente une passe VERS L'AVANT
                    else:
                        mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                        passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                #sinon il va vers la balle faire une passe
                else :
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
            #sinon il se replace
            else:
                #S'il est seul il dézone pou faire une passe
                if (approxi_pos_ball.x <= 2*GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
                else:
                    defense = move.replacement_def(pos_joueur, replacement_def)
                    return defense       
        if s.team == 2:
            #si elle est dans son camp:
            if(approxi_pos_ball.x >= GAME_WIDTH/2):
                #il se met en place pour l'intercepter et fait la passe à l'attaquant
                approxi_pos_ball = s.pos_ball + 6*s.vitesse_ball
                #Si elle est dans la zone du gardien 
                if approxi_pos_ball.x > 4*GAME_WIDTH/5:
                    #Et qu'il a la balle
                    if  near_ball_mate <= near_opp_ball:
                        mouvement = move.appel(pos_joueur, appel_def)
                        return mouvement
                    #sinon il fonce vers la balle et tente une passe VERS L'AVANT
                    else:
                        mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                        passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                #sinon il va vers la balle faire une passe
                else :
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
            #sinon il se replace
            else:
                #S'il est seul il dézone pou faire une passe
                if (approxi_pos_ball.x >= GAME_WIDTH/3) and dist_joueur_ball <= near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
                else:
                    defense = move.replacement_def(pos_joueur, replacement_def)
                    return defense       
        
class Gardien(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_joueur = s.pos_joueur
        pos_ball = s.pos_ball
        pos_cage = s.cage_def
        vect_vitesse_joueur = s.vitesse_joueur
        approxi_pos_ball = s.pos_ball + 2*s.vitesse_ball
        dist_joueur_ball = s.dist_joueur_ball
        near_opp_ball = s.near_opp_ball
        near_mate = s.mate_front[0]
        puissance_tir = 6.
        replacement = s.replacement_gardien
        #s'il est dans l'équipe une:
        if s.team == 1:
            #si la balle est dans la surface:
            if(approxi_pos_ball.x < GAME_WIDTH/4) and ((approxi_pos_ball.y < 4*GAME_HEIGHT/5) and (approxi_pos_ball.y > GAME_HEIGHT/5)):
                mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                tir = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                return mouvement + tir
            #sinon si elle est dans son camp:
            elif(approxi_pos_ball.x <= GAME_WIDTH/2):
                #s'il est le plus proche, il fait une passe
                if dist_joueur_ball < near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else:
                    #sinon il reste en position gardien 
                    defense = move.DeGea_pos(pos_joueur, approxi_pos_ball, pos_cage, vect_vitesse_joueur)
                    return defense
            #sinon il se replace
            else:
                defense = move.replacement_def(pos_joueur, replacement)
                return defense       
        if s.team == 2:
            #si la balle est dans la surface:
            if(approxi_pos_ball.x > 3*GAME_WIDTH/4) and ((approxi_pos_ball.y < 4*GAME_HEIGHT/5) and (approxi_pos_ball.y > GAME_HEIGHT/5)):
                mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                tir = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                return mouvement + tir
            #sinon si elle est dans son camp:
            elif(approxi_pos_ball.x >= GAME_WIDTH/2):
                #s'il est le plus proche, il fait une passe
                if dist_joueur_ball < near_opp_ball:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else:
                    #sinon il reste en position gardien 
                    defense = move.DeGea_pos(pos_joueur, approxi_pos_ball, pos_cage, vect_vitesse_joueur)
                    return defense
            #sinon il se replace
            else:
                defense = move.replacement_def(pos_joueur, replacement)
                return defense
            

class Milieu(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Def")
        
    def compute_strategy(self, state, id_team, id_player):
        s = superstate(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_joueur = s.pos_joueur
        pos_ball = s.pos_ball
        pos_cage = s.cage_def
        cage_adv = s.cage_adv
        puissance_tir = shoot.puissance_tir(6)
        vect_vitesse_joueur = s.vitesse_joueur
        approxi_pos_ball = s.pos_ball + 6*s.vitesse_ball
        near_ball_mate = s.near_mate_ball
        dist_joueur_ball = s.dist_joueur_ball
        near_opp_ball = s.near_opp_ball
        near_mate = s.near_mate[1]
        pos_opp = s.opponents_pos
        zone_pressing = 80
        mate_front = s.mate_front[0]
        shoot_poss = s.shoot_poss(pos_joueur, near_mate)
        pass_poss = s.passe_poss
        opp_opp_balle = s.near_opp2
        appel = s.replacement_att4v4_bas
        centre = s.centre
        if s.team == 1:
            #Si la balle est proche
            if dist_joueur_ball <= zone_pressing:
                #si je suis plus proche de la balle que l'adversaire et qu'elle est dans ma zone, je fais une passe
                if dist_joueur_ball <= near_opp_ball and approxi_pos_ball.x > 2*GAME_WIDTH/5 and pos_ball.x < 3.5*GAME_WIDTH/5:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
                else:
                    #Il se place entre deux adversaires et cherche à faire la passe
                    mouvement = move.joueur_entre_adv(pos_joueur, s.opponents_pos[len(s.opponents_pos)-1], s.opponents_pos[len(s.opponents_pos)-2])
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
            else:
                #Il vient suppleer l'attaquant
                if approxi_pos_ball.x > 3.5*GAME_WIDTH/5:
                    mouvement = move.appel(pos_joueur, appel)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else:
                    #Il se replace au centre
                    mouvement = move.replacement_def(pos_joueur, centre)
                    return mouvement
        else:   
             #Si la balle est proche
            if dist_joueur_ball <= zone_pressing:
                #si je suis plus proche de la balle que l'adversaire et qu'elle est dans ma zone, je fais une passe
                if dist_joueur_ball <= near_opp_ball and approxi_pos_ball.x < 3*GAME_WIDTH/5 and pos_ball.x > 1.5*GAME_WIDTH/5:
                    mouvement = move.joueur_vers_ball(pos_joueur, approxi_pos_ball, vect_vitesse_joueur)
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
                else:
                    #Il se place entre deux adversaires et cherche à faire la passe
                    mouvement = move.joueur_entre_adv(pos_joueur, s.opponents_pos[len(s.opponents_pos)-1], s.opponents_pos[len(s.opponents_pos)-2])
                    passe = shoot.passe2(pos_joueur, mate_front, puissance_tir)
                    return mouvement + passe
            else:
                #Il vient suppleer l'attaquant
                if approxi_pos_ball.x < 1.5*GAME_WIDTH/5:
                    mouvement = move.appel(pos_joueur, appel)
                    passe = shoot.passe2(pos_joueur, near_mate, puissance_tir)
                    return mouvement + passe
                else:
                    #Il se replace au centre
                    mouvement = move.replacement_def(pos_joueur, centre)
                    return mouvement

    """
    # Add players
    team1.add("Ramos", Def2v2())
    team1.add("Mariano", Attaquant2v2())
    team2.add("Zizou", Attaquant2v2())
    team2.add("Ramos", Def2v2())
    

if __name__  == "__main__":
    team1 = SoccerTeam(name="Team 1")
    team2 = SoccerTeam(name="Team 2")


    team1.add("Lopez", Gardien())
    team1.add("Ramos", Def4v4())
    team1.add("Zizou", Milieu())
    team1.add("Mariano", Attaquant4v4())
    team2.add("Lloris", Gardien())
    team2.add("TSilva", Def4v4())
    team2.add("Kaka", Milieu())
    team2.add("Girou", Attaquant4v4())
    
    # Create a match
    simu = Simulation(team1, team2, max_steps = 1000)

    # Simulate and display the match
    show_simu(simu)
    """
