# Feature: Characters Have Classes
# As a player I want a character to have a class that customizes its capabilities so 
# that I can play more interesting characters

from src.models.entity import Entity
from src.models.
import pytest

# LETS TRY SAMPLE 1:
# As a player I want to play a Fighter so that I can kick 
# butt and take names 

# attacks roll is increased by 1 for 
# every level instead of every other level has 10 hit points 
# per level instead of 5

# character ROLE - meaning "fighter", "mage", etc...
# make a class for character roles
# need to make classes that can be passed to any character we create - aka entity
# each class should have its own pre-determined attributes
    # this is so we can later compare these to each other to test...

def test_fighter_hp_advantage():
    fighter = 
