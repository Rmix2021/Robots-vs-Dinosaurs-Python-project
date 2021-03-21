from dinosaur import Dinosaur
from attack import AttackType


class Herd:
    def __init__(self):
        self.herd = [Dinosaur("T-rex", 15000, 200, AttackType("Roaring Bite", 500)), Dinosaur("Raptor", 10000, 1500,
        AttackType("Organ Slash", 250)), Dinosaur("Triceratops", 20000, 750, AttackType('Horn Impalement', 300))]


