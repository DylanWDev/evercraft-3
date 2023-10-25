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
    #hp is currently 10 ---- entity2 is our target - a hit is -2? - so goes down to 8


# as a character i want to accumulate exp points when i attack my enemies so that i can earn bragging rights at the tavern
# when a successful attack occurs the character gains 10 exp

def test_gain_character_xp():
    defender = Entity("Lauren","neutral",4,2)
    attacker = Entity("Dylan","evil", 1,4)
    # doing the attack
    attacker.attack(defender,20)
    assert attacker.xp is 10

# xp acquired when enemy is killed - when entity.hp is 0 or less than 0
# add 10 xp to attacker

# if attacking make 2 characters - an attacker and defender