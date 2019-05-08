Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\GridTest.py ==
soccersimulator.mdpsoccer:DEBUG - Traceback (most recent call last):
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\mdpsoccer.py", line 497, in next_step
    actions.update(t.compute_strategies(self.state, i+1))
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\mdpsoccer.py", line 401, in compute_strategies
    enumerate(self.players) if  hasattr( x.strategy,"compute_strategy")])
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\mdpsoccer.py", line 401, in <listcomp>
    enumerate(self.players) if  hasattr( x.strategy,"compute_strategy")])
  File "C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\Grid.py", line 122, in compute_strategy
    return  shoot.passe2(pos_joueur, pos_mate, self.strength)
  File "C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\projet\actions.py", line 165, in passe2
    return self.shoot_aim(pos_joueur, pos_mate, puissance_tir)
  File "C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\projet\actions.py", line 120, in shoot_aim
    vect_tir_norm = vect_tir.normalize() * puissance_tir
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\utils.py", line 272, in __mul__
    return Vector2D(self.x * other, self.y * other)
TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'

soccersimulator.mdpsoccer:WARNING - unsupported operand type(s) for *: 'float' and 'NoneType'
soccersimulator.mdpsoccer:WARNING - Error for team 1 -- loose match
{'strength': 5}
 Crit : ␣1␣␣␣ Cpt :␣1 
{'strength': 5}
 Crit : ␣1␣␣␣ Cpt :␣2 
{'strength': 5}
 Crit : ␣2␣␣␣ Cpt :␣3 
{'strength': 5}
 Crit : ␣2␣␣␣ Cpt :␣4 
{'strength': 5}
 Crit : ␣2␣␣␣ Cpt :␣5 
{'strength': 5}
 Crit : ␣3␣␣␣ Cpt :␣6 
{'strength': 5}
 Crit : ␣4␣␣␣ Cpt :␣7 
{'strength': 5}
 Crit : ␣5␣␣␣ Cpt :␣8 
{'strength': 5}
 Crit : ␣5␣␣␣ Cpt :␣9 
{'strength': 5}
 Crit : ␣6␣␣␣ Cpt :␣10 
{'strength': 5}
 Crit : ␣6␣␣␣ Cpt :␣11 
{'strength': 5}
 Crit : ␣6␣␣␣ Cpt :␣12 
{'strength': 5}
 Crit : ␣6␣␣␣ Cpt :␣13 
{'strength': 5}
 Crit : ␣7␣␣␣ Cpt :␣14 
{'strength': 5}
 Crit : ␣7␣␣␣ Cpt :␣15 
{'strength': 5}
 Crit : ␣8␣␣␣ Cpt :␣16 
{'strength': 5}
 Crit : ␣9␣␣␣ Cpt :␣17 
{'strength': 5}
 Crit : ␣10␣␣␣ Cpt :␣18 
{'strength': 5}
 Crit : ␣11␣␣␣ Cpt :␣19 
{'strength': 5}
 Crit : ␣12␣␣␣ Cpt :␣20 
{'strength': 5}
 Crit : ␣12␣␣␣ Cpt :␣21 
{'strength': 5}
 Crit : ␣13␣␣␣ Cpt :␣22 
{'strength': 5}
 Crit : ␣13␣␣␣ Cpt :␣23 
{'strength': 5}
 Crit : ␣13␣␣␣ Cpt :␣24 
{'strength': 5}
 Crit : ␣14␣␣␣ Cpt :␣25 
{'strength': 5}
 Crit : ␣15␣␣␣ Cpt :␣26 
{'strength': 5}
 Crit : ␣15␣␣␣ Cpt :␣27 
{'strength': 5}
 Crit : ␣15␣␣␣ Cpt :␣28 
{'strength': 5}
 Crit : ␣15␣␣␣ Cpt :␣29 
{'strength': 5}
 Crit : ␣15␣␣␣ Cpt :␣30 
{'strength': 6}
 Crit : ␣0␣␣␣ Cpt :␣1 
{'strength': 6}
 Crit : ␣1␣␣␣ Cpt :␣2 
{'strength': 6}
 Crit : ␣2␣␣␣ Cpt :␣3 
{'strength': 6}
 Crit : ␣3␣␣␣ Cpt :␣4 
{'strength': 6}
 Crit : ␣3␣␣␣ Cpt :␣5 
{'strength': 6}
 Crit : ␣3␣␣␣ Cpt :␣6 
{'strength': 6}
 Crit : ␣3␣␣␣ Cpt :␣7 
{'strength': 6}
 Crit : ␣3␣␣␣ Cpt :␣8 
{'strength': 6}
 Crit : ␣3␣␣␣ Cpt :␣9 
{'strength': 6}
 Crit : ␣4␣␣␣ Cpt :␣10 
{'strength': 6}
 Crit : ␣5␣␣␣ Cpt :␣11 
{'strength': 6}
 Crit : ␣5␣␣␣ Cpt :␣12 
{'strength': 6}
 Crit : ␣5␣␣␣ Cpt :␣13 
{'strength': 6}
 Crit : ␣6␣␣␣ Cpt :␣14 
{'strength': 6}
 Crit : ␣7␣␣␣ Cpt :␣15 
{'strength': 6}
 Crit : ␣7␣␣␣ Cpt :␣16 
{'strength': 6}
 Crit : ␣8␣␣␣ Cpt :␣17 
{'strength': 6}
 Crit : ␣8␣␣␣ Cpt :␣18 
{'strength': 6}
 Crit : ␣9␣␣␣ Cpt :␣19 
{'strength': 6}
 Crit : ␣9␣␣␣ Cpt :␣20 
{'strength': 6}
 Crit : ␣9␣␣␣ Cpt :␣21 
{'strength': 6}
 Crit : ␣10␣␣␣ Cpt :␣22 
{'strength': 6}
 Crit : ␣11␣␣␣ Cpt :␣23 
{'strength': 6}
 Crit : ␣11␣␣␣ Cpt :␣24 
{'strength': 6}
 Crit : ␣11␣␣␣ Cpt :␣25 
{'strength': 6}
 Crit : ␣11␣␣␣ Cpt :␣26 
{'strength': 6}
 Crit : ␣12␣␣␣ Cpt :␣27 
{'strength': 6}
 Crit : ␣12␣␣␣ Cpt :␣28 
{'strength': 6}
 Crit : ␣12␣␣␣ Cpt :␣29 
{'strength': 6}
 Crit : ␣12␣␣␣ Cpt :␣30 
{(('strength', 5),): 0.5, (('strength', 6),): 0.4}
(('strength', 5),)
Distance entre les joueurs:  40.697051490249265
>>> 
== RESTART: C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\GridTest.py ==
soccersimulator.mdpsoccer:DEBUG - Traceback (most recent call last):
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\mdpsoccer.py", line 497, in next_step
    actions.update(t.compute_strategies(self.state, i+1))
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\mdpsoccer.py", line 401, in compute_strategies
    enumerate(self.players) if  hasattr( x.strategy,"compute_strategy")])
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\mdpsoccer.py", line 401, in <listcomp>
    enumerate(self.players) if  hasattr( x.strategy,"compute_strategy")])
  File "C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\Grid.py", line 122, in compute_strategy
    return  shoot.passe2(pos_joueur, pos_mate, self.strength)
  File "C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\projet\actions.py", line 165, in passe2
    return self.shoot_aim(pos_joueur, pos_mate, puissance_tir)
  File "C:\Users\lepet\OneDrive\Documents\2I013\Soccer\foot\projet\actions.py", line 120, in shoot_aim
    vect_tir_norm = vect_tir.normalize() * puissance_tir
  File "C:\Python36\lib\site-packages\soccersimulator-1.2018.2.1-py3.6.egg\soccersimulator\utils.py", line 272, in __mul__
    return Vector2D(self.x * other, self.y * other)
TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'

soccersimulator.mdpsoccer:WARNING - unsupported operand type(s) for *: 'float' and 'NoneType'
soccersimulator.mdpsoccer:WARNING - Error for team 1 -- loose match
{'strength': 5}
 Crit : ␣0␣␣␣ Cpt :␣1 
{'strength': 5}
 Crit : ␣0␣␣␣ Cpt :␣2 
{'strength': 5}
 Crit : ␣1␣␣␣ Cpt :␣3 
{'strength': 5}
 Crit : ␣1␣␣␣ Cpt :␣4 
{'strength': 5}
 Crit : ␣1␣␣␣ Cpt :␣5 
{'strength': 5}
 Crit : ␣1␣␣␣ Cpt :␣6 
{'strength': 5}
 Crit : ␣1␣␣␣ Cpt :␣7 
{'strength': 5}
 Crit : ␣2␣␣␣ Cpt :␣8 
{'strength': 5}
 Crit : ␣2␣␣␣ Cpt :␣9 
{'strength': 5}
 Crit : ␣2␣␣␣ Cpt :␣10 
{'strength': 5}
 Crit : ␣3␣␣␣ Cpt :␣11 
{'strength': 5}
 Crit : ␣4␣␣␣ Cpt :␣12 
{'strength': 5}
 Crit : ␣5␣␣␣ Cpt :␣13 
{'strength': 5}
 Crit : ␣6␣␣␣ Cpt :␣14 
{'strength': 5}
 Crit : ␣6␣␣␣ Cpt :␣15 
{'strength': 5}
 Crit : ␣6␣␣␣ Cpt :␣16 
{'strength': 5}
 Crit : ␣7␣␣␣ Cpt :␣17 
{'strength': 5}
 Crit : ␣7␣␣␣ Cpt :␣18 
{'strength': 5}
 Crit : ␣8␣␣␣ Cpt :␣19 
{'strength': 5}
 Crit : ␣9␣␣␣ Cpt :␣20 
{'strength': 5}
 Crit : ␣10␣␣␣ Cpt :␣21 
{'strength': 5}
 Crit : ␣11␣␣␣ Cpt :␣22 
{'strength': 5}
 Crit : ␣12␣␣␣ Cpt :␣23 
{'strength': 5}
 Crit : ␣13␣␣␣ Cpt :␣24 
{'strength': 5}
 Crit : ␣14␣␣␣ Cpt :␣25 
{'strength': 5}
 Crit : ␣15␣␣␣ Cpt :␣26 
{'strength': 5}
 Crit : ␣15␣␣␣ Cpt :␣27 
{'strength': 5}
 Crit : ␣16␣␣␣ Cpt :␣28 
{'strength': 5}
 Crit : ␣17␣␣␣ Cpt :␣29 
{'strength': 5}
 Crit : ␣18␣␣␣ Cpt :␣30 
{'strength': 6}
 Crit : ␣0␣␣␣ Cpt :␣1 
{'strength': 6}
 Crit : ␣0␣␣␣ Cpt :␣2 
{'strength': 6}
 Crit : ␣0␣␣␣ Cpt :␣3 
{'strength': 6}
 Crit : ␣0␣␣␣ Cpt :␣4 
{'strength': 6}
 Crit : ␣0␣␣␣ Cpt :␣5 
{'strength': 6}
 Crit : ␣0␣␣␣ Cpt :␣6 
{'strength': 6}
 Crit : ␣1␣␣␣ Cpt :␣7 
{'strength': 6}
 Crit : ␣1␣␣␣ Cpt :␣8 
{'strength': 6}
 Crit : ␣1␣␣␣ Cpt :␣9 
{'strength': 6}
 Crit : ␣2␣␣␣ Cpt :␣10 
{'strength': 6}
 Crit : ␣2␣␣␣ Cpt :␣11 
{'strength': 6}
 Crit : ␣2␣␣␣ Cpt :␣12 
{'strength': 6}
 Crit : ␣3␣␣␣ Cpt :␣13 
{'strength': 6}
 Crit : ␣4␣␣␣ Cpt :␣14 
{'strength': 6}
 Crit : ␣5␣␣␣ Cpt :␣15 
{'strength': 6}
 Crit : ␣5␣␣␣ Cpt :␣16 
{'strength': 6}
 Crit : ␣6␣␣␣ Cpt :␣17 
{'strength': 6}
 Crit : ␣6␣␣␣ Cpt :␣18 
{'strength': 6}
 Crit : ␣6␣␣␣ Cpt :␣19 
{'strength': 6}
 Crit : ␣6␣␣␣ Cpt :␣20 
{'strength': 6}
 Crit : ␣6␣␣␣ Cpt :␣21 
{'strength': 6}
 Crit : ␣6␣␣␣ Cpt :␣22 
{'strength': 6}
 Crit : ␣7␣␣␣ Cpt :␣23 
{'strength': 6}
 Crit : ␣7␣␣␣ Cpt :␣24 
{'strength': 6}
 Crit : ␣7␣␣␣ Cpt :␣25 
{'strength': 6}
 Crit : ␣8␣␣␣ Cpt :␣26 
{'strength': 6}
 Crit : ␣8␣␣␣ Cpt :␣27 
{'strength': 6}
 Crit : ␣8␣␣␣ Cpt :␣28 
{'strength': 6}
 Crit : ␣9␣␣␣ Cpt :␣29 
{'strength': 6}
 Crit : ␣9␣␣␣ Cpt :␣30 
{(('strength', 5),): 0.6, (('strength', 6),): 0.3}
(('strength', 5),)
Distance entre les joueurs:  56.18051263561058
>>> 
