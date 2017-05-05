#!/usr/bin/env python
# -- coding: UTF-8 --

from item import Inventory

class Character(object):

    def __init__(self, health, xp):
        self.health = health
