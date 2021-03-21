from fleet import Fleet
from herd import Herd
import random


def battle(aggressor, defender):
    defender.hit_points -= aggressor.attack_type.attack
    print(f"{aggressor.name} attacks {defender.name}")


def get_random_number(num_1, num_2):
    random_int = random_number(num_1, num_2)
    return random_int


def random_number(min_value, max_value):

    return random.randint(min_value, max_value)


class Battlefield:

    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def auto_fight(self):
        z = 0
        o = 0
        while z <= 3 and o <= 3:
            i = get_random_number(0, 2)
            while self.herd.herd[i].hit_points <= 0:
                i = get_random_number(0, 2)

            m = get_random_number(0, 2)
            while self.fleet.fleet[m].hit_points <= 0:
                m = get_random_number(0, 2)

            n = get_random_number(1, 2)

            if n == 1:
                battle(self.herd.herd[i], self.fleet.fleet[m])
                print(f"{self.herd.herd[i].name} Attacks with {self.herd.herd[i].attack_type.attack_name}")
            if n == 2:
                battle(self.fleet.fleet[m], self.herd.herd[i])
                print(f"{self.fleet.fleet[m].name} Attacks with {self.fleet.fleet[m].attack_type.weapon_name}")
            if self.herd.herd[i].hit_points > 0:
                print(f"{self.herd.herd[i].name}'s Hit-Points = {self.herd.herd[i].hit_points}")
            if self.fleet.fleet[i].hit_points > 0:
                print(f"{self.fleet.fleet[m].name}'s Hit-Points = {self.fleet.fleet[m].hit_points}")

            if self.herd.herd[i].hit_points <= 0:
                print(f"{self.herd.herd[i].name} has been 'Gorified'")
                i += 1
                z += 1

            elif self.fleet.fleet[m].hit_points <= 0:
                print(f"{self.fleet.fleet[m].name} has been 'Destroyed'")
                i += 1
                o += 1

            if z == 3:
                print("Metal Destroys Flesh")
                break
            if o == 3:
                print("Flesh has overcome the Power of Metal")
                break


Battlefield().auto_fight()
