#!/usr/bin/env python
# -- coding: UTF-8 --

from item import Inventory

class Character(object):

    def __init__(self, health, xp):
        self.health = health
        self.xp = xp
        self.position = None

    def eat(self, food):
        self.health += food.use()

    def move(self, cell):
        if self.position != None :
            self.position.characters.remove(self)
        self.position = cell
        self.position.characters.append(self)


    def die(self):
        pass

    def receive_attack(self, damage):
        self.health -= damage


class Player(Character):

    def __init__(self,health,xp):
        Character.__init__(self, health, xp)
        self.inventory = Inventory(20)

    def pick(self, item):
        self.inventory.set_item(item)

    def drop(self, item):
        self.inventory.del_item(item)

    def fight(self, enemy):
        damage = 10
        enemy.receive_attack(damage)

    def receive_attack(self, damage):
        Character.receive_attack(self, damage)


class Chicken(Character):

    def __init__(self):
        Character.__init__(self, 30, 1)
