#from src.models.roles import Fighter
#from src.models.entity import Entity
import numpy as np
import lib.m.roles

import pytest

# Feature: Characters Have Classes
# As a player I want a character to have a class that customizes its capabilities so
# that I can play more interesting chaactersr


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
    # giving fighter its default level 10 and default 5 hp
    fighter = Fighter(10)
    # if the fighter levels up to 2 then its default should be plus 10
    assert fighter.hp is 10
