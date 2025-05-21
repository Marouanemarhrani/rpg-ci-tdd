import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from character import Character

def test_character_initial_hp():
    c = Character()
<<<<<<< HEAD
    assert c.hp == 10
=======
    assert c.hp == 1000
>>>>>>> fa8202c (test failes)

def test_character_death():
    c = Character()
    c.hp = 0
    assert c.is_dead() is True

def test_character_attack():
    a = Character()
    b = Character()
    a.attack(b)
    assert b.hp == 9

def test_character_heal():
    c = Character()
    c.hp = 5
    c.heal()
    assert c.hp == 6

def test_character_cannot_overheal():
    c = Character()
    c.hp = 10
    c.heal()
    assert c.hp == 10

