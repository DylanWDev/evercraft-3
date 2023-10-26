# class template to import into iterations
class Entity:
    def __init__(self, name, alignment, armor_class, hp):
        self.name = name
        # self.character_class = character_class
        self.alignment = alignment
        self.armor_class = armor_class
        self.hp = hp
        self.xp = 0
        self.level = 1

    def increase_xp(self):
        self.xp += 10

    def attack(self, target, roll):
        if roll == 20:
            target.hp -= 2
        elif roll >= target.armor_class:
            target.hp -= 1
        if target.hp <= 0:
            # self = attacker :)
            Entity.increase_xp(self)

    def level_up(self):
        # to be more modular make the leveling up dependent on xp not kill count
        if self.xp % 1000 == 0:
            self.level += 1