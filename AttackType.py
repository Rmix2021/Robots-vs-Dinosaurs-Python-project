
class AttackType:
    def __init__(self, power):
        self.bite.power = power
        self.slice.power = power
        self.swarm.power = power

    def bite(self):
        self.bite.power = 250

    def slice(self):
        self.slice.power = 400

    def swarm(self):
        self.swarm.power = 1000
