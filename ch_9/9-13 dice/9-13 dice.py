from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        h = 0
        print(f"\namount of sides: {self.sides}")
        while h <= 10:
            print(randint(1, self.sides))
            h += 1

my_dice = Die()
my_dice.roll_die()

my_other_dice = Die(10)
my_other_dice.roll_die()

my_dice = Die(20)
my_dice.roll_die()