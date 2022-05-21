from pickle import FALSE
from colorama import Fore, Back, Style
from time import time
# import config as C
from os import system


class king:
    def __init__(self):
        self.damage = 250
        self.health = 1000
        self.speed = 1
        self.x_coord = 0
        self.y_coord = 0
        self.destroyed = FALSE
        self.count = 0
        self.symbol = 'K'
        self.facing = '.'

    def move(self, command):
        if command == 'w':
            self.x_coord -= self.speed
        elif command == 's':
            self.x_coord += self.speed
        elif command == 'a':
            self.y_coord -= self.speed
        elif command == 'd':
            self.y_coord += self.speed

    def rage(self):
        print("Rage spell bitch")
        self.damage = 100
        self.speed = 2
        
    def heal(self, barblist):
        print("Heal spell bitch")
        self.health *= 1.5
        if self.health > 1000:
            self.health = 1000
        for i in barblist:
            i.health *= 1.5
            if i.health > 500:
                i.health = 500
        
