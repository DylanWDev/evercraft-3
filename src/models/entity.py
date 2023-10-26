
class Modifiers:

    modifier = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: +1,
        13: +1,
        14: +2,
        15: +2,
        16: +3,
        17: +3,
        18: +4,
        19: +4,
        20: +5,
    }

    def __init__(self, name, value, modifier):
        self.name = name
        self.value = value
        self.modifier = modifier

# class template to import into iterations
class Entity:

    abilities = {
    "strength": 10,
    "dexterity": 10,
    "constitution": 10,
    "wisdom": 10,
    "intelligence": 10,
    "charisma" : 10,
    }

    def __init__(self, name, alignment, armor_class, hp, **ability):
        self.name = name
        # self.character_class = character_class
        self.alignment = alignment
        self.armor_class = armor_class
        self.hp = hp
        self.xp = 0
        self.level = 1

        for x in self.abilities:
            value = ability[x] if (x in ability) else self.abilities[x] # new variable called value 
            # assigns a value to the  variable called value - uses conditional expression (basically a ternary)
                # ability[x] - loops through our abilities one by one
                # if (x in ability) - checks if within our kwargs that ability exists with a pre-determined number value
                    # if so use that for our entity/character
                # else self.abilities[x] - else if that ability looped through is not 'changed' in our kwargs then use the default ability/value pair listed in Entity class

            mod = Modifiers(x, value, Modifiers.modifier[value])
            # mod creates a new instance of our class Modifiers
                # (x = ability name, value = the number value connected to the ability, ---
                # Modifiers - refers to the class, .modifier[value] - refers to the modifier key value pair)
            
            setattr(self, x, mod)
            # use setattribute to now finally connect within self aka whatever character/entity we create 
                # x represents the abilities we loop through and mod is the newly attached modifier value to the corresponding abilities

# BRAINSTORM FOR LOOP:
# for loop to loop through the abilities within the entity class
# looping over the variable - (default abilities) variable - making a new variable called value
# value = kwargs 
# if key is in abilities - else self.abilities (key)
    # key is x 
# key is i (in terms of iterating through)
# new variable called a = (a new class - of modifier ability values) - takes in 
# set attribute 
# FIRST - make a new class of modifier values 



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

