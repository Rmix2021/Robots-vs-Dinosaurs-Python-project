class Dinosaur:
    def __init__(self, name, hit_points, energy, attack):
        self.name = name
        self.hit_points = hit_points
        self.energy = energy
        self.attack = attack

    def dinosaur_attack(self, robot):
        robot.robot_hit_points -= self.dinosaur_attack
