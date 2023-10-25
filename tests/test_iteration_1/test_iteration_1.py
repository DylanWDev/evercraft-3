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
    entity1 = Entity("big bird") 
    assert entity1.name is "big bird"


# as a character i want to have my alignment so 
# that i have something to guide my actions
    # can get set alignment
    # alignments are good, evil, neutral

def test_create_alignment():
    entity1 = Entity("bob", "good", 16)
    assert entity1.alignment is "good"

# as a combatant i want to have armor class and hit points so that i can resist attacks from my enemies
    # has an armor class that defaults to 10
    # has 5 hit points by default

def test_create_armor_class():
    entity1 = Entity("bob", "good", 16)
    assert entity1.armor_class is 16