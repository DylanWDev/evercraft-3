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

def test_create_alignment():
    entity1 = Entity("bob", "good")
    assert entity1.alignment is "good"