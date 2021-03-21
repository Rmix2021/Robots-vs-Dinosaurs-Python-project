from robot import Robot
from weapon import AttackType


class Fleet:
    def __init__(self):
        self.fleet = [Robot("Devastator", 15000, 200, AttackType("Photon Blasters", 500)), Robot("Incinerator", 10000,
            1500, AttackType("Laser Mini Gun", 250)), Robot("Death Armor", 20000, 750, AttackType("B.F.G", 300))]
