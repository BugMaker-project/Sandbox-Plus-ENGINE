# Copyright (c)2020 BugMaker-Project
# An Interface for Enemys
from pygame import Surface

class Enemy(object):
    def __init__(self,img,canvas,attr:dict,pos:tuple):
        self.img:Surface=img
        self.canvas:Surface=canvas
        self.attr:dict=attr
        self.pos:tuple=pos
    def draw(self):
        pass
    def fight(self):
        pass
    def move(self):
        pass
    def getInfo(self):
        pass
    def isDied(self):
        pass