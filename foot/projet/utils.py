from soccersimulator import Vector2D



def compute_move(pos_joueur, vect_vitesse_joueur, expected_pos):
    vect = expected_pos - pos_joueur
    vect.normalize()
    return  vect

def compute_shoot(aimed_pos, pos_joueur, puissance_tir):
    vect = aimed_pos - pos_joueur
    return vect
"""
pos_ball (96.305591,25.674534)
pos_cage (150.000000,44.350000)
action Acc:(-26.847204,-9.337733),
Shoot:(0.000000,0.000000),
Name:
"""
