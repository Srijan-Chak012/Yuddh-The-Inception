from pickle import FALSE, TRUE
from colorama import Fore, Back, Style
import time
# import config as C
from src.input import *
from os import system
from src.commandking import *

def clear():
    _ = system('clear')


class Balloon:
    def __init__(self):
        self.damage = 200
        self.health = 501
        self.speed = 2
        self.x = 0
        self.y = 0
        self.destroyed = FALSE
        self.symbol = 'P'
    
    def balloon_spawn(self, arr, x, y, Buildings, king1):
        arr[x][y] = "\033[31m" + 'P' + "\033[0m"
        self.x = x
        self.y = y
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        self.balloon_move(arr, Buildings, king1)

    def balloon_move(self, arr, Buildings, king1):
        # print(Buildings)
        # exit()
        if not Buildings:
            return
        if self.destroyed == TRUE:
            return
        dist = {}
        height = len(arr)
        width = len(arr[0])
        if ("\033[92m" + 'C' + "\033[0m" in x for x in arr) or ("\033[93m" + 'C' + "\033[0m" in x for x in arr) or ("\033[91m" + 'C' + "\033[0m" in x for x in arr) or ("\033[92m" + 'M' + "\033[0m" in x for x in arr) or ("\033[93m" + 'M' + "\033[0m" in x for x in arr) or ("\033[91m" + 'M' + "\033[0m" in x for x in arr):
            for i in range(height):
                for j in range(width):
                    if arr[i][j] == "\033[92m" + 'C' + "\033[0m" or arr[i][j] == "\033[93m" + 'C' + "\033[0m" or arr[i][j] == "\033[91m" + 'C' + "\033[0m" or arr[i][j] == "\033[92m" + 'M' + "\033[0m" or arr[i][j] == "\033[93m" + 'M' + "\033[0m" or arr[i][j] == "\033[91m" + 'M' + "\033[0m":
                        dist[(i, j)] = abs(self.x - i) + abs(self.y - j)
            print(dist)
            # input()
        if not dist:
            # print(dist)
            # exit()
            for i in range(height):
                for j in range(width):
                    if arr[i][j] != '.' and (arr[i][j] != "\033[33m" + 'A' + "\033[0m" and arr[i][j] != "\033[32m" + 'A' + "\033[0m" and arr[i][j] != "\033[31m" + 'A' + "\033[0m") and (arr[i][j] != "\033[33m" + 'P' + "\033[0m" and arr[i][j] != "\033[32m" + 'P' + "\033[0m" and arr[i][j] != "\033[31m" + 'P' + "\033[0m") and (arr[i][j] != "\033[33m" + 'B' + "\033[0m" and arr[i][j] != "\033[32m" + 'B' + "\033[0m" and arr[i][j] != "\033[31m" + 'B' + "\033[0m") and arr[i][j] != '#' and (arr[i][j] != "\033[32m" + 'K' + "\033[0m" and arr[i][j] != "\033[33m" + 'K' + "\033[0m" and arr[i][j] != "\033[31m" + 'K' + "\033[0m") and (arr[i][j] != "\033[32m" + 'Q' + "\033[0m" and arr[i][j] != "\033[33m" + 'Q' + "\033[0m" and arr[i][j] != "\033[31m" + 'Q' + "\033[0m") and arr[i][j] != "\033[32m" + 'W' + "\033[0m" and arr[i][j] != "\033[33m" + 'W' + "\033[0m" and arr[i][j] != "\033[31m" + 'W' + "\033[0m":
                        dist[(i, j)] = abs(i - self.x) + abs(j - self.y)
        print(dist)
        if not dist:
            return
        min_dist = min(dist, key=dist.get)
        # print(Buildings[(min_dist[0], min_dist[1])].name)
        # exit()
        if min_dist[0] >= self.x and min_dist[1] >= self.y:
            for i in range(self.x, min_dist[0]-1):
                if self.y == 0 or self.y == width - 1:
                    arr[i][self.y] = '#'
                else :
                    key = (i, self.y)
                    if key in Buildings.keys():
                        Buildings[key].draw(Buildings[key].starting_x, Buildings[key].starting_y, arr)
                    else:
                        arr[i][self.y] = '.'
                if arr[i+1][self.y] == '#' or arr[i+1][self.y] == '.':
                    if self.health > 150 and self.health <= 500:
                        arr[i+1][self.y] = "\033[32m" + 'P' + "\033[0m"
                    if self.health > 50 and self.health <= 150:
                        arr[i+1][self.y] = "\033[33m" + 'P' + "\033[0m"
                    else:
                        # if self.health > 0 and self.health <= 200:
                        arr[i+1][self.y] = "\033[31m" + 'P' + "\033[0m"
                self.x = i+1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king1.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)     
                break
            # time.sleep(0.3)
            for i in range(self.y, min_dist[1]-1):
                if self.y == 0:
                    arr[self.x][i] = '#'
                else :
                    key = (self.x, i)
                    if key in Buildings.keys():
                        Buildings[key].draw(Buildings[key].starting_x, Buildings[key].starting_y, arr)
                    else:
                        arr[self.x][i] = '.'
                if self.health > 150 and self.health <= 500:
                    arr[self.x][i+1] = "\033[32m" + 'P' + "\033[0m"
                if self.health > 50 and self.health <= 150:
                    arr[self.x][i+1] = "\033[33m" + 'P' + "\033[0m"
                else:
                    # if self.health > 0 and self.health <= 200:
                    arr[self.x][i+1] = "\033[31m" + 'P' + "\033[0m"
                self.y = i+1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)   
                break
                # time.sleep(0.1)
            # print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            # print("Here")barb_move
            if self.x == min_dist[0]-1 and self.y == min_dist[1]-1:
                self.balloon_attack(arr, Buildings, min_dist[0], min_dist[1], king1)

        elif min_dist[0] >= self.x and min_dist[1] <= self.y:
            for i in range(self.x, min_dist[0]-1):
                if self.y == 0 or self.y == width - 1:
                    arr[i][self.y] = '#'
                else :
                    key = (i, self.y)
                    if key in Buildings.keys():
                        Buildings[key].draw(Buildings[key].starting_x, Buildings[key].starting_y, arr)
                    else:
                        arr[i][self.y] = '.'
                if arr[i+1][self.y] == '#' or arr[i+1][self.y] == '.':
                    if self.health > 150 and self.health <= 500:
                        arr[i+1][self.y] = "\033[32m" + 'P' + "\033[0m"
                    if self.health > 50 and self.health <= 150:
                        arr[i+1][self.y] = "\033[33m" + 'P' + "\033[0m"
                    else:
                        # if self.health > 0 and self.health <= 200:
                        arr[i+1][self.y] = "\033[31m" + 'P' + "\033[0m"
                self.x = i+1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)     
                break
            # time.sleep(0.3)
            for i in range(self.y, min_dist[1]+1, -1):
                if self.y == 0:
                    arr[self.x][i] = '#'
                else :
                    key = (self.x, i)
                    if key in Buildings.keys():
                        Buildings[key].draw(Buildings[key].starting_x, Buildings[key].starting_y, arr)
                    else:
                        arr[self.x][i] = '.'
                if arr[self.x][i-1] == '#' or arr[self.x][i-1] == '.':
                    if self.health > 150 and self.health <= 500:
                        arr[self.x][i-1] = "\033[32m" + 'P' + "\033[0m"
                    if self.health > 50 and self.health <= 150:
                        arr[self.x][i-1] = "\033[33m" + 'P' + "\033[0m"
                    else:
                        # if self.health > 0 and self.health <= 200:
                        arr[self.x][i-1] = "\033[31m" + 'P' + "\033[0m"
                self.y = i-1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)     
                break
                # time.sleep(0.1)
            # print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            # print("Here")
            if self.x == min_dist[0]-1 and self.y == min_dist[1]+1:
                self.balloon_attack(arr, Buildings, min_dist[0], min_dist[1], king1)

        elif min_dist[0] <= self.x and min_dist[1] >= self.y:
            if self.y == 0 or self.y == width - 1:
                arr[self.x][self.y] = '#'
            else:
                key = (self.x, self.y)
                if key in Buildings.keys():
                    Buildings[key].draw(Buildings[key].starting_x, Buildings[key].starting_y, arr)
                else:
                    arr[self.x][self.y] = '.'
            for i in range(self.x, min_dist[0]+1, -1):
                if self.health > 150 and self.health <= 500:
                    arr[i-1][self.y] = "\033[32m" + 'P' + "\033[0m"
                if self.health > 50 and self.health <= 150:
                    arr[i-1][self.y] = "\033[33m" + 'P' + "\033[0m"
                else:
                    # if self.health > 0 and self.health <= 200:
                    arr[i-1][self.y] = "\033[31m" + 'P' + "\033[0m"
                self.x = i-1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)     
                break
        
            for i in range(self.y, min_dist[1]-1):
                if self.y == 0:
                    arr[self.x][i] = '#'
                else :
                    key = (self.x, i)
                    if key in Buildings.keys():
                        Buildings[key].draw(Buildings[key].starting_x, Buildings[key].starting_y, arr)
                    else:
                        arr[self.x][i] = '.'
                if self.health > 150 and self.health <= 500:
                    arr[self.x][i+1] = "\033[32m" + 'P' + "\033[0m"
                if self.health > 50 and self.health <= 150:
                    arr[self.x][i+1] = "\033[33m" + 'P' + "\033[0m"
                else:
                    # if self.health > 0 and self.health <= 200:
                    arr[self.x][i+1] = "\033[31m" + 'P' + "\033[0m"
                self.y = i+1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)     
                break
                # time.sleep(0.1)
            # print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            # print("Here")
            if self.x == min_dist[0]+1 and self.y == min_dist[1]-1:
                self.balloon_attack(arr, Buildings, min_dist[0], min_dist[1], king1)

        elif min_dist[0] <= self.x and min_dist[1] <= self.y:
            for i in range(self.x, min_dist[0]+1, -1):
                if self.y == 0 or self.y == width - 1:
                    arr[i][self.y] = '#'
                else :
                    key = (i, self.y)
                    if key in Buildings.keys():
                        arr[i][self.y] = Buildings[key].symbol
                    else:
                        arr[i][self.y] = '.'
                if self.health > 150 and self.health <= 500:
                    arr[i-1][self.y] = "\033[32m" + 'P' + "\033[0m"
                if self.health > 50 and self.health <= 150:
                    arr[i-1][self.y] = "\033[33m" + 'P' + "\033[0m"
                else:
                    # if self.health > 0 and self.health <= 200:
                    arr[i-1][self.y] = "\033[31m" + 'P' + "\033[0m"
                self.x = i-1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)    
                break
            # time.sleep(0.3)
            for i in range(self.y, min_dist[1]+1, -1):
                if self.y == 0:
                    arr[self.x][i] = '#'
                else :
                    key = (self.x, i)
                    if key in Buildings.keys():
                        arr[self.x][i] = Buildings[key].symbol
                    else:
                        arr[self.x][i] = '.'
                if self.health > 150 and self.health <= 500:
                    arr[self.x][i-1] = "\033[32m" + 'P' + "\033[0m"
                if self.health > 50 and self.health <= 150:
                    arr[self.x][i-1] = "\033[33m" + 'P' + "\033[0m"
                else:
                    # if self.health > 0 and self.health <= 200:
                    arr[self.x][i-1] = "\033[31m" + 'P' + "\033[0m"
                self.y = i-1
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)     
                break
                # time.sleep(0.1)
            # print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            # print("Here")
            if self.x == min_dist[0]+1 and self.y == min_dist[1]+1:
                self.balloon_attack(arr, Buildings, min_dist[0], min_dist[1], king1)
        return min_dist

    def balloon_attack(self, arr, Buildings, x, y, king1):
        # clear()
        attackedbuilding = Buildings[(x, y)] #Here, Change kar chutiye
        print(attackedbuilding.name)
        if attackedbuilding.health > 0:
            system('aplay -q music/archer.wav&')
            print("Health = " + str(attackedbuilding.health))
            print(Fore.YELLOW + 'Damage done to the ' + attackedbuilding.name + ' is ' + str(self.damage) + Fore.RESET)
            attackedbuilding.health -= self.damage
            if(attackedbuilding.health > 0):
                print("Health = " + str(attackedbuilding.health))
                attackedbuilding.draw(attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
            else:
                print("Health = 0")
                attackedbuilding.destroyed = True
                for i in attackedbuilding.points:
                    if Buildings[i] == attackedbuilding:
                        del Buildings[i]
                attackedbuilding.draw(attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
            clear()
            print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            if king1.health > 0:
                    remaining = int(king1.health/20)
                    health = '♥' * remaining
                    print("Player's health: " +  health)     
            # time.sleep(0.1)
            # clear()
        # clear()

            
        
