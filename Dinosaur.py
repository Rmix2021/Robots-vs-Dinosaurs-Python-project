import AttackType

class Dinosaur:
    def __init__(self, name, power, weapon_power):
        self.name = name
        self.hit_points = 20000
        self.power = 1500

    def set_name(self):
        self.name = input("Name your Dinosaur.")
        print("This Dinosaur is ", self.name)



