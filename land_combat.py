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



    def _reinforce_divisions_in_combat(self):
        # pull division out of reserve
        while self.attackers_reserve:
            at_div = pop_div(self.attackers_reserve)

            if (self.attackers_width+at_div.width)<self.max_width:
                self.attackers_width += at_div.width
                if random.random()<0.02:
                    self.attackers_active.append(at_div)
                else:
                    self.attackers_reserve.append(at_div)
            else:
                self.attackers_reserve.append(at_div)
                break

        while self.defenders_reserve:
            def_div = pop_div(self.defenders_reserve)
            if (self.defenders_width+def_div.width)<self.max_width:
                self.defenders_width += def_div.width
                if random.random()<0.02:
                    self.defenders_active.append(def_div)
                else:
                    self.defenders_reserve.append(def_div)
            else:
                self.defenders_reserve.append(def_div)
                break



    
    def simulate_combat(self) -> str:
        def distribute_attack(division:Division, ennemy_div_list:List[Division]):
            target_width = division.get_width()*2
            targets_list = []

            for ennemy_division in random.sample(ennemy_div_list, len(ennemy_div_list)): 
                if ennemy_division.get_width() <= target_width:
                    target_width -= ennemy_division.get_width()

                    priority =(division.get_soft_attack()*(1-ennemy_division.get_hardness()) + division.get_hard_attack()*(ennemy_division.get_hardness())*1.2)*(1-ennemy_division.get_org_ratio()/4)*(1-0.5*(division.get_piercing()<ennemy_division.get_armour()))
                    targets_list.append((ennemy_division, priority))
                    targets_list = sorted(targets_list, key = lambda x:x[1])

            if not targets_list:
                targets_list.append((random.choice(ennemy_div_list), 0))

            targets_list[0][0].add_attack(Attack(division.get_soft_attack()*0.35, division.get_hard_attack()*0.35, division.get_piercing(), division.get_armour()))
            for (target_div, _) in targets_list:
                target_div.add_attack(Attack(division.get_soft_attack()*0.65/len(targets_list), division.get_hard_attack()*0.65/len(targets_list), division.get_piercing(), division.get_armour()))
        

        self._push_divisions_in_combat()

   

        while self.attackers_active and self.defenders_active:

            for attacker in self.attackers_active:
                distribute_attack(attacker, self.defenders_active)

            for defender in self.defenders_active:
                distribute_attack(defender, self.attackers_active)


            for attacker in self.attackers_active:
                attacker.take_damage(is_defender=False)

            for defender in self.defenders_active:
                defender.take_damage(is_defender=True)

            for attacker in self.attackers_active:
                if not attacker.is_alive():
                    self.attackers_active.remove(attacker)
            
            for defender in self.defenders_active:
                if not self.defenders_active:
                    self.defenders_active.remove(defender)

            self._reinforce_divisions_in_combat()



        # Determine winner
        if self.attackers_active and not self.defenders_active:
            return "Attacker wins"
        elif self.defenders_active and not self.attackers_active:
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