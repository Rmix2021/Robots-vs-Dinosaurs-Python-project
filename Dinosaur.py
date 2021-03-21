class Dinosaur:
    def __init__(self, name, hit_points, energy, attack_type):
        self.name = name
        self.hit_points = hit_points
        self.energy = energy
        self.attack_type = attack_type

    def dinosaur_attack(self, robot):
        robot.robot_hit_points -= self.dinosaur_attack
