from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.fleet = [Robot("Devastator", 15000, 200, Weapon("Photon Blasters", 500)), Robot("Incinerator", 10000,
            1500, Weapon("Laser Mini Gun", 250)), Robot("Death Armor", 20000, 750, Weapon("B.F.G", 300))]
