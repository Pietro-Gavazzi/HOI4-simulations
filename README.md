# HOI4-simulations
I'm doing this project to simulate land combat, navy combat, economy and so on for my personal games.to make some simulations on hoi4 combat, feel free to fork this 

If not stated othrwise, the source for the mechanics will be paradox wiki: https://hoi4.paradoxwikis.com/

NB: don't search necessarely for readable or optimised code, I'm a junior developper 


## Land combat:
source: https://hoi4.paradoxwikis.com/Land_battle


## uresolved cases 

### no implementation: effect of being half strength

### no calculation of damage taken after battle

### defense
Immagine an infantry division in defense is in combat with one infantry and one tank division in attack, the attacking tank division cannot be pierced.
Immagine the defending division has 200 defense, the infantry attacking division 80 soft attack and the tank division 300 soft attack.
How is the defense applied to counter the atacks, is it 100 defense for each divisions or something else ?
the problem is that because the tank cannot be pierced, attacks coming from the tank have another dice for damage 
and i wans asking myself what happens in "mixed  combat" where some of the attack comes from the infantry (that can be pierced) and some comes from the tank
so my question is more: when we have hits, how many have the 1,2,3,4 organisation dice and how many the 1,2,3,4,5,6 organisation dice ? 

### chosen division in active combat, begin combat

for now they are chosen at randomµ

### chosen targetted division
each turn reinitialise targetted divisions