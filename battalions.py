from dataclasses import dataclass


@dataclass
class Battalion:
    name: str
    soft_attack: float
    hard_attack: float
    defense: float
    breakthrough: float
    armour:float
    piercing:float
    hp: float
    max_org: float
    hardness: float
    width: float
    type: str  # "infantry", "armor", "artillery", etc.


# Example battalions
inf = Battalion("Infantry", 
                soft_attack=6, 
                hard_attack=1, 
                defense=22, 
                breakthrough=3, 
                piercing = 1,
                armour = 0,
                hp=25, 
                max_org=60, 
                hardness=0, 
                width=2,
                type="infantry"
                )
art = Battalion("Artillery", 
                soft_attack=25, 
                hard_attack=2, 
                defense=10, 
                breakthrough=6, 
                piercing = 5,
                armour = 0,
                hp=.6, 
                max_org=0, 
                hardness=0, 
                width=3, 
                type="artillery"
                )
motorised = Battalion("Motorised", 
                soft_attack=6, 
                hard_attack=1, 
                defense=22, 
                breakthrough=3, 
                piercing = 1,
                armour = 0,
                hp=25, 
                max_org=60, 
                hardness=.2, 
                width=2, 
                type="mobile"
                )

light_tank = Battalion("Light Tank", 
                       soft_attack=13, 
                       hard_attack=4, 
                       defense=4, 
                       breakthrough=29.9, 
                       piercing = 10,
                       armour = 10,
                       hp=2, 
                       max_org=10,  
                       hardness=.8, 
                       width=2, 
                       type="armor"
                       )