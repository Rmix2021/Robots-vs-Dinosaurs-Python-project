class Robot:
    def __init__(self, name, hit_points, battery_power, weapon):
        self.name = name
        self.hit_points = hit_points
        self.battery_power = battery_power
        self.weapon = weapon

    def robot_attack(self, dinosaur):
        dinosaur.dinosaur_hit_points -= self.robot_attack
