from divisions import *
from battalions import *
from utils import round, dice

import numpy as np
import random


class CombatScenario():
    def __init__(self, attacker_div, defender_div):
        self.attacker = attacker_div
        self.defender = defender_div



    

    def simulate_combat(self, hours: int = 200*24) -> str:
       
        for hour in range(hours):
            if not (self.attacker.is_alive() and self.defender.is_alive()):
                break

            # Attacker attacks
            atk_soft_att = self.attacker._total_stat("soft_attack")
            atk_hard_att = self.attacker._total_stat("hard_attack")
            atk_piercing = self.attacker.get_piercing() 
            atk_armour = self.attacker.get_armour() 

            self.defender.take_damage(atk_soft_att, atk_hard_att, atk_piercing, atk_armour, is_defender=True)

            # Defender counters
            def_soft_att = self.defender._total_stat("soft_attack")
            def_hard_att = self.defender._total_stat("hard_attack")
            def_piercing = self.defender.get_piercing() 
            def_armour = self.defender.get_armour() 

            self.attacker.take_damage(def_soft_att, def_hard_att, def_piercing, def_armour, is_defender=False)

        # Determine winner
        if self.attacker.is_alive() and not self.defender.is_alive():
            return "Attacker wins"
        elif self.defender.is_alive() and not self.attacker.is_alive():
            return "Defender wins"
        else:
            return "Stalemate"
