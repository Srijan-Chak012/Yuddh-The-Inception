from pickle import FALSE, TRUE
from colorama import Fore, Back, Style
from time import time
# import config as C
from os import system
from src.barbarians import *

def clear():
    _ = system('clear')

class Building:
    def __init__(self, height, width, name, symbol):
        self.height = height
        self.width = width
        self.health = 1000
        self.name = name
        self.symbol = symbol
        self.underattack = FALSE
        self.points = set()
        self.destroyed = FALSE   
    def draw(self, starting_x, starting_y, arr):
        if self.destroyed == FALSE:
            self.starting_x = starting_x
            self.starting_y = starting_y
            for i in range(self.height):
                for j in range(self.width):
                    if self.health > 500 and self.health <= 1000:
                        arr[i + starting_x][j + starting_y] = "\033[32m" + self.symbol + "\033[0m" 
                    elif self.health > 200 and self.health <= 500:
                        arr[i + starting_x][j + starting_y] = "\033[33m" + self.symbol + "\033[0m"
                    else:
                        # if self.health > 0 and self.health <= 200:
                        arr[i + starting_x][j + starting_y] = "\033[31m" + self.symbol + "\033[0m"
                    self.points.add((i + starting_x, j + starting_y))
        else:
            self.color = Fore.WHITE
            for i in range(self.height):
                for j in range(self.width):
                    arr[i + starting_x][j + starting_y] = '.'
                    self.points.remove((i + starting_x, j + starting_y))

class Wall(Building):
    def __init__(self, height, width, name, symbol):
        super().__init__(height, width, 'Wall', 'W')
        self.health = 200
    
    def draw(self, starting_x, starting_y, arr):
        if self.destroyed == FALSE:
            self.starting_x = starting_x
            self.starting_y = starting_y
            for i in range(self.height):
                for j in range(self.width):
                    if self.health > 500 and self.health <= 1000:
                        arr[i + starting_x][j + starting_y] = "\033[32m" + self.symbol + "\033[0m" 
                    elif self.health > 200 and self.health <= 500:
                        arr[i + starting_x][j + starting_y] = "\033[33m" + self.symbol + "\033[0m"
                    else:
                        # if self.health > 0 and self.health <= 200:
                        arr[i + starting_x][j + starting_y] = "\033[31m" + self.symbol + "\033[0m"
                    self.points.add((i + starting_x, j + starting_y))
        else:
            self.color = Fore.WHITE
            for i in range(self.height):
                for j in range(self.width):
                    arr[i + starting_x][j + starting_y] = '.'
                    self.points.remove((i + starting_x, j + starting_y))

class Defense:
    def __init__(self, height, width, name, symbol):
        self.height = height
        self.width = width
        self.health = 1000
        self.damage = 200
        self.name = name
        self.symbol = symbol
        self.underattack = FALSE
        self.points = set()
        self.destroyed = FALSE 

    def draw(self, starting_x, starting_y, arr):
        if self.destroyed == FALSE:
            self.starting_x = starting_x
            self.starting_y = starting_y
            for i in range(self.height):
                for j in range(self.width):
                    if self.health > 500 and self.health <= 1000:
                        arr[i + starting_x][j + starting_y] = "\033[92m" + self.symbol + "\033[0m" 
                    elif self.health > 200 and self.health <= 500:
                        arr[i + starting_x][j + starting_y] = "\033[93m" + self.symbol + "\033[0m"
                    else:
                        # if self.health > 0 and self.health <= 200:
                        arr[i + starting_x][j + starting_y] = "\033[91m" + self.symbol + "\033[0m"
                    self.points.add((i + starting_x, j + starting_y))
        else:
            self.color = Fore.WHITE
            for i in range(self.height):
                for j in range(self.width):
                    arr[i + starting_x][j + starting_y] = '.'
                    self.points.remove((i + starting_x, j + starting_y))

    def attack(self, arr, trooplist, barblist, archlist, king):
        if self.destroyed == FALSE:
            if king.destroyed == FALSE:
                if (abs(king.x_coord - int((self.starting_x + self.starting_x + self.height)/2)) + abs(king.y_coord - int((self.starting_y + self.starting_y + self.width)/2))) < 6:
                    system('aplay -q music/canonshot.wav&')

                    king.health -= self.damage
                    if king.health <= 0:
                        king.health = 0
                        king.destroyed = TRUE
                        arr[king.x_coord][king.y_coord] = '.'
                    
                    clear()
                    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                    if king.health > 0:
                        remaining = int(king.health/20)
                        health = '♥' * remaining
                        print("Player's health: " +  health)  
                    # print(king.health)
            troops = trooplist
            for i in trooplist:
                if i.destroyed == FALSE:
                    if (abs(i.x - int(( self.starting_x + self.starting_x + self.height)/2)) + abs(i.y - int((self.starting_y + self.starting_y + self.width)/2))) < 6:     
                        system('aplay -q music/canonshot.wav&')
                        if i.health > 0:
                            i.health -= self.damage
                        if i.health <= 0:
                            i.health = 0
                            i.destroyed = TRUE
                            arr[i.x][i.y] = '.'
                            troops.remove(i)
                            if i.symbol == 'B':
                                barblist.remove(i)
                            elif i.symbol == 'A':
                                archlist.remove(i)
                        clear()
                        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                        if king.health > 0:
                            remaining = int(king.health/20)
                            health = '♥' * remaining
                            print("Player's health: " +  health)  
                        # print(i.health)
            if king.destroyed == TRUE and not troops: 
                return [], [], []
            else:
                return troops, barblist, archlist
        else:
            return trooplist, barblist, archlist

class Wizard:
    def __init__(self, height, width, name, symbol):
        self.height = height
        self.width = width
        self.health = 1000
        self.damage = 200
        self.name = name
        self.symbol = symbol
        self.underattack = FALSE
        self.points = set()
        self.destroyed = FALSE 
    
    def draw(self, starting_x, starting_y, arr):
        if self.destroyed == FALSE:
            self.starting_x = starting_x
            self.starting_y = starting_y
            for i in range(self.height):
                for j in range(self.width):
                    if self.health > 500 and self.health <= 1000:
                        arr[i + starting_x][j + starting_y] = "\033[92m" + self.symbol + "\033[0m" 
                    elif self.health > 200 and self.health <= 500:
                        arr[i + starting_x][j + starting_y] = "\033[93m" + self.symbol + "\033[0m"
                    else:
                        # if self.health > 0 and self.health <= 200:
                        arr[i + starting_x][j + starting_y] = "\033[91m" + self.symbol + "\033[0m"
                    self.points.add((i + starting_x, j + starting_y))
        else:
            self.color = Fore.WHITE
            for i in range(self.height):
                for j in range(self.width):
                    arr[i + starting_x][j + starting_y] = '.'
                    self.points.remove((i + starting_x, j + starting_y))
    
    def attack(self, arr, trooplist, barblist, archlist, balloonlist, king):
        if self.destroyed == FALSE:
            troops = trooplist
            if king.destroyed == FALSE:
                if (abs(king.x_coord - int((self.starting_x + self.starting_x + self.height)/2)) + abs(king.y_coord - int((self.starting_y + self.starting_y + self.width)/2))) < 6:
                    system('aplay -q music/wizardshot.wav&')
                    if king.health > 0:
                        king.health -= self.damage
                        if king.health <= 0:
                            king.health = 0
                            king.destroyed = TRUE
                            arr[king.x_coord][king.y_coord] = '.'
                    min_x = king.x_coord - 1
                    min_y = king.y_coord - 1
                    max_x = king.x_coord + 1
                    max_y = king.y_coord + 1
                    if min_x < 0:
                        min_x = 0
                    if min_y < 0:
                        min_y = 0
                    if max_x > len(arr) - 1:
                        max_x = len(arr) - 1
                    if max_y > len(arr[0]) - 1:
                        max_y = len(arr[0]) - 1
                    for x in range(min_x, max_x + 1):
                        for y in range(min_y, max_y + 1):
                            for troop in troops:
                                if troop.destroyed == FALSE:
                                    if troop.x == x and troop.y == y:
                                        troop.health -= self.damage
                                        if troop.health <= 0:
                                            troop.health = 0
                                            troop.destroyed = TRUE
                                            arr[troop.x][troop.y] = '.'
                                            troops.remove(troop)
                                            if troop.symbol == 'B':
                                                barblist.remove(troop)
                                            elif troop.symbol == 'A':
                                                archlist.remove(troop)
                                            elif troop.symbol == 'P':
                                                balloonlist.remove(troop)
                    
            for i in trooplist:
                if i.destroyed == FALSE:
                    if (abs(i.x - int(( self.starting_x + self.starting_x + self.height)/2)) + abs(i.y - int((self.starting_y + self.starting_y + self.width)/2))) < 6:     
                        system('aplay -q music/wizardshot.wav&')
                        # if i.health > 0:
                        #     i.health -= self.damage
                        # if i.health <= 0:
                        #     i.health = 0
                        #     i.destroyed = TRUE
                        #     arr[i.x][i.y] = '.'
                        #     troops.remove(i)
                        min_x = i.x - 1
                        min_y = i.y - 1
                        max_x = i.x + 1
                        max_y = i.y + 1
                        if min_x < 0:
                            min_x = 0
                        if min_y < 0:
                            min_y = 0
                        if max_x > len(arr) - 1:
                            max_x = len(arr) - 1
                        if max_y > len(arr[0]) - 1:
                            max_y = len(arr[0]) - 1
                        for x in range(min_x, max_x + 1):
                            for y in range(min_y, max_y + 1):
                                for troop in troops:
                                    if troop.destroyed == FALSE:
                                        if troop.x == x and troop.y == y:
                                            troop.health -= self.damage
                                            if troop.health <= 0:
                                                troop.health = 0
                                                troop.destroyed = TRUE
                                                arr[troop.x][troop.y] = '.'
                                                troops.remove(troop)
                                                if troop.symbol == 'B':
                                                    barblist.remove(troop)
                                                elif troop.symbol == 'A':
                                                    archlist.remove(troop)
                                                elif troop.symbol == 'P':
                                                    balloonlist.remove(troop)

                                if king.destroyed == FALSE:
                                    print(king.x_coord, king.y_coord)
                                    # exit()
                                    if king.x_coord == x and king.y_coord == y:
                                        king.health -= self.damage
                                        if king.health <= 0:
                                            king.health = 0
                                            king.destroyed = TRUE
                                            arr[king.x][king.y] = '.'

            clear()
            print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            if king.health > 0:
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)  
                        # print(i.health)
            
            if king.destroyed == TRUE and not troops:
                return [], [], [], []
            else: 
                return troops, barblist, archlist, balloonlist
        else:
            return trooplist, barblist, archlist, balloonlist

