from Weapon import Weapon
class Robot:
    def __init__(self, name) :
        self.name = name
        self.hit_points = 20000
        self.power = 1000
        self.robot_weapon = Weapon("Laser Blaster")

    #attack
    def roboAttack(self, dino):
        dino.hitpoints = dino.hitpoints - self.power













