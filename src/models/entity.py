# class template to import into iterations
class Entity:
    def __init__(self, name, alignment, armor_class, hp):
        self.name = name
        # self.character_class = character_class
        self.alignment = alignment
        self.armor_class = armor_class
        self.hp = hp
    def attack(self, target, roll):
        if roll >= target.armor_class:
            target.hp -= 2
