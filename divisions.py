from typing import List, Dict
import numpy as np
import random
from utils import dice, round
from battalions import *

class Division():
    name: str
    battalions: List[Battalion]
    hp:float
    org:float

    def __init__(self, name, battalions):
        self.name = name
        self.battalions = battalions
        self.org = np.mean([getattr(b, "org") for b in self.battalions])
        self.hp = sum(getattr(b, "org") for b in self.battalions)
    
    def _total_stat(self, stat: str) -> float:
        return sum(getattr(b, stat) for b in self.battalions)
    
    def get_piercing(self):
        return .4*max([getattr(b, "piercing") for b in self.battalions]) + .6*np.mean([getattr(b, "piercing") for b in self.battalions])
    
    def get_armour(self):
        return .4*max([getattr(b, "armour") for b in self.battalions]) + .6*np.mean([getattr(b, "armour") for b in self.battalions])
        
    
    def get_hardness(self):
        return np.mean([getattr(b, "hardness") for b in self.battalions])


    def take_damage(self, soft_att: float, hard_att: float, other_piercing:float, other_armour:float, is_defender:bool):

        hardness = self.get_hardness()
        hard_mod_attack = (soft_att * (1-hardness) + hard_att * hardness)

        attack = round(hard_mod_attack)
        if (is_defender): 
            defence = round(self._total_stat("defense"))
        else:
            defence = round(self._total_stat("breakthrough"))


        defended_attacks = min(attack, defence)
        undefended_attack = max(attack-defence, 0)

        hits = sum(random.random()<0.1 for _ in range(defended_attacks)) +  sum(random.random()<0.4 for _ in range(undefended_attack))
        if other_piercing>=self.get_armour():
            pierced_coef = 1
        elif other_piercing >=self.get_armour()*0.75:
            pierced_coef = 0.8
        elif other_piercing >=self.get_armour()*0.5:
            pierced_coef = 0.65
        elif other_piercing<self.get_armour()*0.5:
            pierced_coef = 0.5
        else: 
            print("error piercing")
            exit(1)


        self.hp -= dice(2)*hits*0.06*0.1 *pierced_coef

        if self.get_piercing()<other_armour*0.5:
            self.org -= dice(6)*hits*0.053*0.1*pierced_coef
        else:
            self.org -= dice(4)*hits*0.053*0.1*pierced_coef




    def is_alive(self) -> bool:
        return self.org > 0 and self.hp > 0

    


