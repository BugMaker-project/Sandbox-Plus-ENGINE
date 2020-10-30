# Copyright (c)2020 BugMaker-Project
# An Interface for players
from pygame import Surface

class Player(object):
    def __init__(self,img,canvas,attr:dict,pos:tuple):
        self.img:Surface=img
        self.canvas:Surface=canvas
        self.attr:dict=attr
        self.backpack:list=[[] for i in range(10)]
        self.pos:tuple=pos
    def draw(self):
        pass
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