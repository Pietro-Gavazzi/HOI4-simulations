from divisions import *
from battalions import *
from terrain import *
from utils import *

import numpy as np
import random

def pop_div(x: List[Division]) -> Division:
    elem = random.choice(x)
    x.remove(elem)
    return elem



class CombatScenario():

    attackers_reserve:List[Division]
    defenders_reserve = List[Division]
    terrain=Terrain
    width = int
    max_width = int
    attackers_active = List[Division]
    defenders_active = List[Division]
    attackers_width = int
    defenders_width = int

    def __init__(self, attacker_divs:list, defender_divs:list, terrain:Terrain):
        self.attackers_reserve = attacker_divs
        self.defenders_reserve = defender_divs
        self.terrain=terrain
        self.width = self.terrain.base_width
        self.max_width = self.width*(4/3)
        self.attackers_active = []
        self.defenders_active = []
        self.attackers_width = 0
        self.defenders_width = 0



    def _push_divisions_in_combat(self):
        # pull division out of reserve
        while self.attackers_reserve:
            at_div = pop_div(self.attackers_reserve)

            if (self.attackers_width+at_div.width)<self.max_width:
                self.attackers_width += at_div.width
                self.attackers_active.append(at_div)
            else:
                self.attackers_reserve.append(at_div)
                break

        while self.defenders_reserve:
            def_div = pop_div(self.defenders_reserve)
            if (self.defenders_width+def_div.width)<self.max_width:
                self.defenders_width += def_div.width
                self.defenders_active.append(def_div)
            else:
                self.defenders_reserve.append(def_div)
                break




    def simulate_combat(self) -> str:
        self._push_divisions_in_combat()

        return
    

    

        while self.attackers_active and self.defenders_active:



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



def main():
    terrain = plain
    # Division examples
    division_1 = Division("Infantry Division", [inf]*10 + [art]*0)
    division_2 = Division("Tank Division", [light_tank]*1 + [inf]*0)

    division_1.get_armour()
    division_1.get_piercing()
    # Combat scenario
    battle = CombatScenario([division_2], [division_1], terrain)
    result = battle.simulate_combat()
    print(result)

if __name__=="__main__":
    main()