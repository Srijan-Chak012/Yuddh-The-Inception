from itertools import count
from pickle import FALSE, TRUE
from symtable import Symbol
from typing import Counter
from colorama import Fore, Back, Style
# import config as C
from os import system
from src.building import *
from src.input import *
from src.king import *
from src.barbarians import *
import time


rows = 30
cols = 60

global counter
counter = 0
def clear():
    _ = system('clear')

UnderAttack = set()
def movew(arr, Buildings, king):
    if king.destroyed == TRUE:
        return
    if king.x_coord > 0 and king.y_coord >= 0 and (arr[king.x_coord-1][king.y_coord] == '#' or arr[king.x_coord-1][king.y_coord] == '.'):
        clear()
        # print(king.x_coord, king.y_coord)
        if king.x_coord == 0 or king.y_coord == 0 or king.x_coord == rows-1 or king.y_coord == cols-1:
            # print("Bababooey")
            arr[king.x_coord][king.y_coord] = '#'
        else:
            # print("Hey there")
            arr[king.x_coord][king.y_coord] = '.'

        king.move('w')
        if king.health > 500 and king.health <= 1000:
            arr[king.x_coord][king.y_coord] = "\033[32m" + king.symbol + "\033[0m" 
        elif king.health > 200 and king.health <= 500:
            arr[king.x_coord][king.y_coord] = "\033[33m" + king.symbol + "\033[0m"
        else:
            # if self.health > 0 and self.health <= 200:
            arr[king.x_coord][king.y_coord] = "\033[31m" + king.symbol + "\033[0m"
        
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)  
        # print(king.x_coord, king.y_coord)
    elif arr[king.x_coord-1][king.y_coord] == "\033[34m" + 'B' + "\033[0m":
        clear()
        print(Fore.YELLOW + 'Barbarian present' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
    else:
        clear()
        print(Fore.YELLOW + 'Not allowed to go there' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    # print(king.facing) 
    king.facing = 'w'
    # print(king.facing) 
    # exit()

def moves(arr, Buildings, king):
    if king.destroyed == TRUE:
        return
    if king.x_coord < (rows-1) and king.y_coord >= 0 and (arr[king.x_coord+1][king.y_coord] == '#' or arr[king.x_coord+1][king.y_coord] == '.'):
        clear()
        # print(king.x_coord, king.y_coord)
        if king.x_coord == 0 or king.y_coord == 0 or king.x_coord == rows-1 or king.y_coord == cols-1:
            # print("Bababooey")
            arr[king.x_coord][king.y_coord] = '#'
        else:
            # print("Hey there")
            arr[king.x_coord][king.y_coord] = '.'

        king.move('s')
        if king.health > 500 and king.health <= 1000:
            arr[king.x_coord][king.y_coord] = "\033[32m" + king.symbol + "\033[0m" 
        elif king.health > 200 and king.health <= 500:
            arr[king.x_coord][king.y_coord] = "\033[33m" + king.symbol + "\033[0m"
        else:
            # if self.health > 0 and self.health <= 200:
            arr[king.x_coord][king.y_coord] = "\033[31m" + king.symbol + "\033[0m"
        
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)  
        # print(king.x_coord, king.y_coord)
    elif king.x_coord == rows - 1:
        clear()
        print(Fore.YELLOW + 'Not allowed to go there' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)

    elif arr[king.x_coord+1][king.y_coord] == "\033[34m" + 'B' + "\033[0m":
        clear()
        print(Fore.YELLOW + 'Barbarian present' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    else:
        clear()
        print(Fore.YELLOW + 'Not allowed to go there' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    king.facing = 's'

def movea(arr, Buildings, king):
    if king.destroyed == TRUE:
        return
    if king.x_coord >= 0 and king.y_coord > 0 and (arr[king.x_coord][king.y_coord-1] == '#' or arr[king.x_coord][king.y_coord-1] == '.'):
        clear()
        # print(king.x_coord, king.y_coord)
        if king.x_coord == 0 or king.y_coord == 0 or king.x_coord == rows-1 or king.y_coord == cols-1:
            # print("Bababooey")
            arr[king.x_coord][king.y_coord] = '#'
        else:
            # print("Hey there")
            arr[king.x_coord][king.y_coord] = '.'

        king.move('a')
        if king.health > 500 and king.health <= 1000:
            arr[king.x_coord][king.y_coord] = "\033[32m" + king.symbol + "\033[0m" 
        elif king.health > 200 and king.health <= 500:
            arr[king.x_coord][king.y_coord] = "\033[33m" + king.symbol + "\033[0m"
        else:
            # if self.health > 0 and self.health <= 200:
            arr[king.x_coord][king.y_coord] = "\033[31m" + king.symbol + "\033[0m"
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
        # print(king.x_coord, king.y_coord)
    elif arr[king.x_coord][king.y_coord-1] == "\033[34m" + 'B' + "\033[0m":
        clear()
        print(Fore.YELLOW + 'Barbarian present' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
    else:
        clear()
        print(Fore.YELLOW + 'Not allowed to go there' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
    king.facing = 'a'

def moved(arr, Buildings, king):
    if king.destroyed == TRUE:
        return
    if king.x_coord >= 0 and king.y_coord < cols-1 and (arr[king.x_coord][king.y_coord+1] == '#' or arr[king.x_coord][king.y_coord+1] == '.'):
        clear()
        # print(king.x_coord, king.y_coord)
        if king.x_coord == 0 or king.y_coord == 0 or king.x_coord == rows-1 or king.y_coord == cols-1:
            # print("Bababooey")
            arr[king.x_coord][king.y_coord] = '#'
        else:
            # print("Hey there")
            arr[king.x_coord][king.y_coord] = '.'

        king.move('d')
        if king.health > 500 and king.health <= 1000:
            arr[king.x_coord][king.y_coord] = "\033[32m" + king.symbol + "\033[0m" 
        elif king.health > 200 and king.health <= 500:
            arr[king.x_coord][king.y_coord] = "\033[33m" + king.symbol + "\033[0m"
        else:
            # if self.health > 0 and self.health <= 200:
            arr[king.x_coord][king.y_coord] = "\033[31m" + king.symbol + "\033[0m"
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
        # print(king.x_coord, king.y_coord)

    elif king.y_coord == cols - 1:
        clear()
        print(Fore.YELLOW + 'Not allowed to go there' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
    elif arr[king.x_coord][king.y_coord+1] == "\033[34m" + 'B' + "\033[0m":
        clear()
        print(Fore.YELLOW + 'Barbarian present' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    else:
        clear()
        print(Fore.YELLOW + 'Not allowed to go there' + Fore.RESET)
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)  
    king.facing = 'd'

def kingattack(arr, Buildings, king):
    if king.destroyed == TRUE:
        return
    if king.symbol == "K":
        if (arr[king.x_coord+1][king.y_coord] == '.' or arr[king.x_coord+1][king.y_coord] == '#') and (arr[king.x_coord-1][king.y_coord] == '.' or arr[king.x_coord-1][king.y_coord] == '#') and (arr[king.x_coord][king.y_coord+1] == '.' or arr[king.x_coord][king.y_coord+1] == '#') and (arr[king.x_coord][king.y_coord-1] == '.' or arr[king.x_coord][king.y_coord-1] == '#') :
            return
    else:
        print(king.symbol)
        if king.symbol == "K":
            if arr[king.x_coord+1][king.y_coord] != '.' and arr[king.x_coord+1][king.y_coord] != '#' and arr[king.x_coord+1][king.y_coord] != "\033[34m" + 'B' + "\033[0m":
                attackedbuilding = Buildings[(king.x_coord+1, king.y_coord)]
                if(attackedbuilding.health > 0):
                    print("Health = " + str(attackedbuilding.health))
                    print(Fore.YELLOW + 'Damage done to the ' +
                            attackedbuilding.name + ' is ' + str(king.damage) + Fore.RESET)
                    attackedbuilding.health -= king.damage
                    if(attackedbuilding.health > 0):
                        print("Health = " + str(attackedbuilding.health))
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                    else:
                        print("Health = 0")
                        attackedbuilding.destroyed = True
                        for i in attackedbuilding.points:
                            if Buildings[i] == attackedbuilding:
                                del Buildings[i]
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)

            elif arr[king.x_coord-1][king.y_coord] != '.' and arr[king.x_coord-1][king.y_coord] != '#' and arr[king.x_coord-1][king.y_coord] != 'B':
                attackedbuilding = Buildings[(king.x_coord-1, king.y_coord)]
                if(attackedbuilding.health > 0):
                    print("Health = " + str(attackedbuilding.health))
                    print(Fore.YELLOW + 'Damage done to the ' +
                            attackedbuilding.name + ' is ' + str(king.damage) + Fore.RESET)
                    attackedbuilding.health -= king.damage
                    if(attackedbuilding.health > 0):
                        print("Health = " + str(attackedbuilding.health))
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                    else:
                        print("Health = 0")
                        attackedbuilding.destroyed = True
                        for i in attackedbuilding.points:
                            if Buildings[i] == attackedbuilding:
                                del Buildings[i]
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)
            
            elif arr[king.x_coord][king.y_coord+1] != '.' and arr[king.x_coord][king.y_coord+1] != '#' and arr[king.x_coord][king.y_coord+1] != 'B':
                attackedbuilding = Buildings[(king.x_coord, king.y_coord+1)]
                if(attackedbuilding.health > 0):
                    print("Health = " + str(attackedbuilding.health))
                    print(Fore.YELLOW + 'Damage done to the ' +
                            attackedbuilding.name + ' is ' + str(king.damage) + Fore.RESET)
                    attackedbuilding.health -= king.damage
                    if(attackedbuilding.health > 0):
                        print("Health = " + str(attackedbuilding.health))
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                    else:
                        print("Health = 0")
                        attackedbuilding.destroyed = True
                        for i in attackedbuilding.points:
                            if Buildings[i] == attackedbuilding:
                                del Buildings[i]
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)
            
            elif arr[king.x_coord][king.y_coord-1] != '.' and arr[king.x_coord][king.y_coord-1] != '#' and arr[king.x_coord][king.y_coord-1] != 'B':
                attackedbuilding = Buildings[(king.x_coord, king.y_coord-1)]
                if(attackedbuilding.health > 0):
                    print("Health = " + str(attackedbuilding.health))
                    print(Fore.YELLOW + 'Damage done to the ' +
                            attackedbuilding.name + ' is ' + str(king.damage) + Fore.RESET)
                    attackedbuilding.health -= king.damage
                    if(attackedbuilding.health > 0):
                        print("Health = " + str(attackedbuilding.health))
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                    else:
                        print("Health = 0")
                        attackedbuilding.destroyed = True
                        for i in attackedbuilding.points:
                            if Buildings[i] == attackedbuilding:
                                del Buildings[i]
                        attackedbuilding.draw(
                            attackedbuilding.starting_x, attackedbuilding.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)
        elif king.symbol == "Q":
            #Attack area of 5x5 8 units away
            if king.facing == 'w':
                centre_x = king.x_coord-8
                centre_y = king.y_coord
                if centre_x < 0:
                    centre_x = 0
                if centre_y < 0:
                    centre_y = 0
                min_x = centre_x - 5
                min_y = centre_y - 5
                if min_x < 0:
                    min_x = 0
                if min_y < 0:
                    min_y = 0
                max_x = centre_x + 5
                max_y = centre_y + 5
                if max_x > len(arr):
                    max_x = len(arr)
                if max_y > len(arr[0]):
                    min_y = len(arr[0])

                buildingset = set()
                for i in range(min_x, max_x):
                    for j in range(min_y, max_y):
                        key = (i, j)
                        if key in Buildings.keys():
                            buildingset.add(Buildings[(i, j)])
                        else:
                            continue
                # print(centre_x)
                # print(centre_y)
                # print(min_x)
                # print(min_y)
                # print(max_x)
                # print(max_y)
                # print(buildingset)
                for i in buildingset:
                    i.health -= king.damage
                    if i. health > 0:
                        i.draw(i.starting_x, i.starting_y, arr)
                    else:
                        i.destroyed = True
                        for j in i.points:
                            if Buildings[j] == i:
                                del Buildings[j]
                        i.draw(i.starting_x, i.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)

            elif king.facing == 's': 
                centre_x = king.x_coord+8
                centre_y = king.y_coord
                if centre_x > len(arr):
                    centre_x = len(arr)
                if centre_y > len(arr[0]):
                    centre_y = len(arr[0])
                min_x = centre_x - 5
                min_y = centre_y - 5
                if min_x < 0:
                    min_x = 0
                if min_y < 0:
                    min_y = 0
                max_x = centre_x + 5
                max_y = centre_y + 5
                if max_x > len(arr):
                    max_x = len(arr)
                if max_y > len(arr[0]):
                    min_y = len(arr[0])

                buildingset = set()
                for i in range(min_x, max_x):
                    for j in range(min_y, max_y):
                        key = (i, j)
                        if key in Buildings.keys():
                            buildingset.add(Buildings[(i, j)])
                        else:
                            continue

                for i in buildingset:
                    i.health -= king.damage
                    if i. health > 0:
                        i.draw(i.starting_x, i.starting_y, arr)
                    else:
                        i.destroyed = True
                        for j in i.points:
                            if Buildings[j] == i:
                                del Buildings[j]
                        i.draw(i.starting_x, i.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)
            
            elif king.facing == 'a':
                centre_x = king.x_coord
                centre_y = king.y_coord-8
                if centre_x < 0:
                    centre_x = 0
                if centre_y < 0:
                    centre_y = 0
                min_x = centre_x - 5
                min_y = centre_y - 5
                if min_x < 0:
                    min_x = 0
                if min_y < 0:
                    min_y = 0
                max_x = centre_x + 5
                max_y = centre_y + 5
                if max_x > len(arr):
                    max_x = len(arr)
                if max_y > len(arr[0]):
                    min_y = len(arr[0])

                buildingset = set()
                for i in range(min_x, max_x):
                    for j in range(min_y, max_y):
                        key = (i, j)
                        if key in Buildings.keys():
                            buildingset.add(Buildings[(i, j)])
                        else:
                            continue

                for i in buildingset:
                    i.health -= king.damage
                    if i. health > 0:
                        i.draw(i.starting_x, i.starting_y, arr)
                    else:
                        i.destroyed = True
                        for j in i.points:
                            if Buildings[j] == i:
                                del Buildings[j]
                        i.draw(i.starting_x, i.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)
        
            elif king.facing == 'd':
                centre_x = king.x_coord
                centre_y = king.y_coord+8
                if centre_x > len(arr):
                    centre_x = len(arr)
                if centre_y > len(arr[0]):
                    centre_y = len(arr[0])
                min_x = centre_x - 5
                min_y = centre_y - 5
                if min_x < 0:
                    min_x = 0
                if min_y < 0:
                    min_y = 0
                max_x = centre_x + 5
                max_y = centre_y + 5
                if max_x > len(arr):
                    max_x = len(arr)
                if max_y > len(arr[0]):
                    min_y = len(arr[0])

                buildingset = set()
                for i in range(min_x, max_x):
                    for j in range(min_y, max_y):
                        key = (i, j)
                        if key in Buildings.keys():
                            buildingset.add(Buildings[(i, j)])
                        else:
                            continue

                for i in buildingset:
                    i.health -= king.damage
                    if i. health > 0:
                        i.draw(i.starting_x, i.starting_y, arr)
                    else:
                        i.destroyed = True
                        for j in i.points:
                            if Buildings[j] == i:
                                del Buildings[j]
                        i.draw(i.starting_x, i.starting_y, arr)
                clear()
                print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
                remaining = int(king.health/20)
                health = '♥' * remaining
                print("Player's health: " +  health)

def axe(arr, Buildings, king):
    if king.destroyed == TRUE:
        return
    if king.count != 0:
        clear()
        print("Leviathan axe used")
        print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
        remaining = int(king.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
        return
    if (arr[king.x_coord+1][king.y_coord] == '.' or arr[king.x_coord+1][king.y_coord] == '#') and (arr[king.x_coord-1][king.y_coord] == '.' or arr[king.x_coord-1][king.y_coord] == '#') and (arr[king.x_coord][king.y_coord+1] == '.' or arr[king.x_coord][king.y_coord+1] == '#') and (arr[king.x_coord][king.y_coord-1] == '.' or arr[king.x_coord][king.y_coord-1] == '#') and (arr[king.x_coord+1][king.y_coord+1] == '.' or arr[king.x_coord+1][king.y_coord+1] == '#') and (arr[king.x_coord-1][king.y_coord-1] == '.' or arr[king.x_coord-1][king.y_coord-1] == '#') and (arr[king.x_coord+1][king.y_coord-1] == '.' or arr[king.x_coord+1][king.y_coord-1] == '#') and (arr[king.x_coord-1][king.y_coord+1] == '.' or arr[king.x_coord-1][king.y_coord+1] == '#'):
        # print("No enemies in range")
        king.count += 1
        return
    else:
        for i in range(king.x_coord-1, king.x_coord+2 ,1):
            for j in range(king.y_coord-1, king.y_coord+1 ,1):
                if i == king.x_coord-1 or i == king.x_coord+1 or j == king.y_coord-1 or j == king.y_coord+1:
                    if (i,j) in Buildings:
                        UnderAttack.add(Buildings[(i,j)])
        
        for i in UnderAttack:
            if i.health > 0:
                print("Health = " + str(i.health))
                print(Fore.YELLOW + 'Damage done to the ' +
                        i.name + ' is ' + str(king.damage) + Fore.RESET)
                i.health -= king.damage
                if(i.health > 0):
                    print("Health = " + str(i.health))
                    i.draw(i.starting_x, i.starting_y, arr)
                else:
                    print("Health = 0")
                    i.destroyed = True
                    for j in i.points:
                        if Buildings[j] == i:
                            del Buildings[j]
                    i.draw(i.starting_x, i.starting_y, arr)
            clear()
            print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            remaining = int(king.health/20)
            health = '♥' * remaining
            print("Player's health: " +  health)  

def eagle(arr, Buildings, king):
    if king.symbol == "Q":
        #Attack area of 5x5 8 units away
        if king.facing == 'w':
            centre_x = king.x_coord-16
            centre_y = king.y_coord
            if centre_x < 0:
                centre_x = 0
            if centre_y < 0:
                centre_y = 0
            min_x = centre_x - 9
            min_y = centre_y - 9
            if min_x < 0:
                min_x = 0
            if min_y < 0:
                min_y = 0
            max_x = centre_x + 9
            max_y = centre_y + 9
            if max_x > len(arr):
                max_x = len(arr)
            if max_y > len(arr[0]):
                min_y = len(arr[0])

            buildingset = set()
            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    key = (i, j)
                    if key in Buildings.keys():
                        buildingset.add(Buildings[(i, j)])
                    else:
                        continue
            # print(centre_x)
            # print(centre_y)
            # print(min_x)
            # print(min_y)
            # print(max_x)
            # print(max_y)
            # print(buildingset)
            time.sleep(1)
            for i in buildingset:
                i.health -= king.damage
                if i. health > 0:
                    i.draw(i.starting_x, i.starting_y, arr)
                else:
                    i.destroyed = True
                    for j in i.points:
                        if Buildings[j] == i:
                            del Buildings[j]
                    i.draw(i.starting_x, i.starting_y, arr)
            clear()
            print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            remaining = int(king.health/20)
            health = '♥' * remaining
            print("Player's health: " +  health)

        elif king.facing == 's': 
            centre_x = king.x_coord + 16
            centre_y = king.y_coord
            if centre_x > len(arr):
                centre_x = len(arr)
            if centre_y > len(arr[0]):
                centre_y = len(arr[0])
            min_x = centre_x - 9
            min_y = centre_y - 9
            if min_x < 0:
                min_x = 0
            if min_y < 0:
                min_y = 0
            max_x = centre_x + 9
            max_y = centre_y + 9
            if max_x > len(arr):
                max_x = len(arr)
            if max_y > len(arr[0]):
                min_y = len(arr[0])

            buildingset = set()
            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    key = (i, j)
                    if key in Buildings.keys():
                        buildingset.add(Buildings[(i, j)])
                    else:
                        continue
            time.sleep(1)
            for i in buildingset:
                i.health -= king.damage
                if i. health > 0:
                    i.draw(i.starting_x, i.starting_y, arr)
                else:
                    i.destroyed = True
                    for j in i.points:
                        if Buildings[j] == i:
                            del Buildings[j]
                    i.draw(i.starting_x, i.starting_y, arr)
            clear()
            print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            remaining = int(king.health/20)
            health = '♥' * remaining
            print("Player's health: " +  health)
        
        elif king.facing == 'a':
            centre_x = king.x_coord
            centre_y = king.y_coord - 16
            if centre_x < 0:
                centre_x = 0
            if centre_y < 0:
                centre_y = 0
            min_x = centre_x - 9
            min_y = centre_y - 9
            if min_x < 0:
                min_x = 0
            if min_y < 0:
                min_y = 0
            max_x = centre_x + 9
            max_y = centre_y + 9
            if max_x > len(arr):
                max_x = len(arr)
            if max_y > len(arr[0]):
                min_y = len(arr[0])

            buildingset = set()
            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    key = (i, j)
                    if key in Buildings.keys():
                        buildingset.add(Buildings[(i, j)])
                    else:
                        continue
            
            time.sleep(1)
            for i in buildingset:
                i.health -= king.damage
                if i. health > 0:
                    i.draw(i.starting_x, i.starting_y, arr)
                else:
                    i.destroyed = True
                    for j in i.points:
                        if Buildings[j] == i:
                            del Buildings[j]
                    i.draw(i.starting_x, i.starting_y, arr)
            clear()
            print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            remaining = int(king.health/20)
            health = '♥' * remaining
            print("Player's health: " +  health)
    
        elif king.facing == 'd':
            centre_x = king.x_coord
            centre_y = king.y_coord + 16
            if centre_x > len(arr):
                centre_x = len(arr)
            if centre_y > len(arr[0]):
                centre_y = len(arr[0])
            min_x = centre_x - 9
            min_y = centre_y - 9
            if min_x < 0:
                min_x = 0
            if min_y < 0:
                min_y = 0
            max_x = centre_x + 9
            max_y = centre_y + 9
            if max_x > len(arr):
                max_x = len(arr)
            if max_y > len(arr[0]):
                min_y = len(arr[0])

            buildingset = set()
            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    key = (i, j)
                    if key in Buildings.keys():
                        buildingset.add(Buildings[(i, j)])
                    else:
                        continue

            time.sleep(1)
            for i in buildingset:
                i.health -= king.damage
                if i. health > 0:
                    i.draw(i.starting_x, i.starting_y, arr)
                else:
                    i.destroyed = True
                    for j in i.points:
                        if Buildings[j] == i:
                            del Buildings[j]
                    i.draw(i.starting_x, i.starting_y, arr)
            clear()
            print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
            remaining = int(king.health/20)
            health = '♥' * remaining
            print("Player's health: " +  health)
