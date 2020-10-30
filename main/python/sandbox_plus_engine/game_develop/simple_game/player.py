# Copyright (c)2020 BugMaker-Project
# An Interface for players
from pygame import Surface

class Player(object):
    def __init__(self):
        self.img:Surface=None
        self.canvas:Surface=None
        self.attr:dict={}
        self.backpack:list=[[] for i in range(10)]
        self.pos:tuple=(0,1)
    def fight(self):
        pass
    def move(self):
        pass
    def drink(self):
        pass
    def eat(self):
        pass
    def getInfo(self):
        pass
    def isDied(self):
        pass