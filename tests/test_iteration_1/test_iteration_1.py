from src.models.entity import Entity
import pytest  #

# Feature: Create a Character
# As a character I want to have a name so that I can be distinguished from other characters
# can get and set Name

# created example entity with passed name, class, and alignment

# entity1 = Entity("Big Bird")
# print(entity1)


# test if we can assign input name as entity1 name
def test_create_character():
    entity1 = Entity("big bird", "good", 16, 10)
    assert entity1.name is "big bird"


# as a character i want to have my alignment so
# that i have something to guide my actions
# can get set alignment
# alignments are good, evil, neutral


def test_create_alignment():
    entity1 = Entity("bob", "good", 16, 10)
    assert entity1.alignment is "good"


# as a combatant i want to have armor class and hit points so that i can resist attacks from my enemies
# has an armor class that defaults to 10, 0
# has 5 hit points by default


def test_create_armor_class():
    entity1 = Entity("bob", "good", 16, 10)
    assert entity1.armor_class is 16


# as a combatant I want to be able to attack other combatants so that I can
# survive to fight another day
# roll a 20 sided die (don't code the die)
# roll must meet or beat oponents armor class to hit
# a natural roll of 20 always hits


#######################
# need to write an if else statement - if 20 = hit if <20 then miss


def test_character_attack():
    entity1 = Entity("bob", "good", 16, 10)

    # attack_roll = 0
    # do_attack_roll = False

    # if attack_roll >= armor_class:

    # entity 2 - defender character
    entity2 = Entity("fred", "evil", 18, 10)
    # need to do a dice roll to see if we have an attack
    # entity1 does a dice roll -  has to be greater than entity2's 18

    entity1.attack(entity2, 18)
    # is roll >= .armorclass --- if it is then hit - if not nope
    assert entity2.hp is 9
    # hp is currently 10 ---- entity2 is our target - a hit is -2? - so goes down to 8


# as a character i want to accumulate exp points when i attack my enemies so that i can earn bragging rights at the tavern
# when a successful attack occurs the character gains 10 exp


def test_gain_character_xp():
    defender = Entity("Lauren", "neutral", 4, 2)
    attacker = Entity("Dylan", "evil", 1, 4)
    # doing the attack
    attacker.attack(defender, 20)
    assert attacker.xp is 10


# xp acquired when enemy is killed - when entity.hp is 0 or less than 0
# add 10 xp to attacker

# if attacking make 2 characters - an attacker and defender

# -----------------------------------------------------------

# Feature: A Character Can Level
# As a character I want my experience points to increase my level and combat
#   capabilities so that I can bring vengeance to my foes

# Level defaults to 1
# After 1000 experience points, the character gains a level
# 0 xp -> 1st Level
# 1000 xp -> 2nd Level
# 2000 xp -> 3rd Level
# etc.
# For each level:
# hit points increase by 5 plus Constitution modifier
# 1 is added to attack roll for every even level achieved


def test_character_leveling():
    entity1 = Entity("billy", "Good", 15, 10)
    assert entity1.level is 1


# for every 100 kills you gain 1000 xp
# when xp is divisible by 1000 ++level to entity


# as a character I want to have several abilities so I'm not identical to other characters except in name
# abilities are strngth, dexterity, constitution, wisdom, intelligence, charisma
# Abilities range from 1 to 20 and default to 10
# Abilities have modifiers according to the following table

# example:
# score:      ability modifier:
# 1                   -5
# 2                   -4
# 3                   -4
# 4                   -3
# 5                   -3
# 6                   -2
# 7                   -2
# 8                   -1
# 9                   -1
# 10                   0
# 11                   0
# 12                  +1
# 13                  +1
# 14                  +2
# 15                  +2
# 16                  +3
# 17                  +3
# 18                  +4
# 19                  +4
# 20                  +5


def test_ability_modifier():
    entity1 = Entity("billy", "Good", 15, 10)
    assert entity1.strength is not None


# default ability value... (aka strength = 10)
# what happens when we add a modifier to that default ability value

# attributes should already be within the entity function
# test if the entity has the attributes? - like testing if the entity has a name
# test to see if null...

# pass kwargs in and for loop through the kwargs and check if strength matches and if does
# grab value and check dictionary for modifiers and grab modifier value and set it to strength value
# for character

# when you create character do a loop to rewrite the values of attributes for that character


def test_ability_dexterity():
    entity1 = Entity("billy", "Good", 15, 10)
    assert entity1.dexterity.value is 10


def test_ability_mod_strength():
    entity1 = Entity("billy", "Good", 15, 10)
    assert entity1.strength.modifier is 0


def test_given_ability_mod_constitution():
    entity1 = Entity("billy", "Good", 15, 10, constitution = 4)
    assert entity1.constitution.modifier is -3

def test_two_given_abilities():
    entity1 =Entity("billy", "good", 15, 10, constitution = 6, dexterity = 9)
    assert entity1.constitution.modifier is -2 and entity1.dexterity.modifier is -1



