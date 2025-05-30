from dataclasses import dataclass

@dataclass
class Terrain:
    name: str
    base_width:int
    added_width:int

plain = Terrain(
    name="plain",
    base_width= 70,
    added_width= 35,
)