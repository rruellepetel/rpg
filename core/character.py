#!/usr/bin/env python
# -- coding: UTF-8 --

from item import Inventory

class Character(object):

    def __init__(self, health, xp):
        self.health = health
        self.xp = xp

    def eat(self, food):
        self.health += food.use()

    def move(self):
        pass

    def die(self):
        pass

    def received_attack(self, damage):
        self.health -= damage


class Player(Character):

    def __init__(self,health,xp):
        Character.__init__(health, xp)
        self.inventory = Inventory(50)

    def pick(self, item):
        self.inventory.add_item(item)

    def drop(self, item):
        self.inventory.remove_item(item)

    def fight(self, character):
        damage = 0
        character.received_attack(damage)

    def received_attack(self, damage):
        Character.received_attack(self, damage)


class Chicken(Character):

    def __init__(self):
        Character.__init__(30, 1)
