from dinosaur import Dinosaur
from attack import Attack


class Herd:
    def __init__(self):
        self.herd = [Dinosaur("T-rex", 15000, 200, Attack("Roaring Bite", 500)), Dinosaur("Raptor", 10000, 1500, Attack
        ("Organ Slash", 250)), Dinosaur("Triceratops", 20000, 750, Attack('Horn Impalement', 300))]
