from colorama import Fore, Back, Style
# import config as C
from os import system
from src.balloon import Balloon
from src.building import *
from src.input import *
from src.king import *
from src.barbarians import Barbarian
from src.archers import Archer
import time

rows = 30
cols = 60

Barbarian_list = []
Archer_list = []
Balloon_list = []

def clear():
    _ = system('clear')

def exit0():
    print('You have exited the game')

def spawn1(arr, Buildings, king1):
    clear()
    print('Your spawn point is present at (first row, first column)')
    arr[0][0] = '#'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Barbarian_single = Barbarian()
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)  
    Barbarian_single.barb_spawn(arr, 1, 1, Buildings, king1)
    Barbarian_list.append(Barbarian_single)
    spawn_x = 1
    spawn_y = 1
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    return Barbarian_list

def spawn2(arr, Buildings, king1):
    clear()
    print('You spawn point is present at (middle row, last column)')
    arr[0][0] = '#'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Barbarian_single = Barbarian()
    Barbarian_single.barb_spawn(arr, int(rows/2)-1, cols-2, Buildings, king1)
    Barbarian_list.append(Barbarian_single)
    spawn_x = int(rows/2)-1
    spawn_y = cols-2
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
    return Barbarian_list

def spawn3(arr, Buildings, king1):
    clear()
    print('You spawn point is present at (last row, last column)')
    arr[1][1] = '.'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Barbarian_single = Barbarian()
    Barbarian_single.barb_spawn(arr, rows-2, int(cols/2)-1, Buildings, king1)
    Barbarian_list.append(Barbarian_single)
    spawn_x = int(cols/2)-1
    spawn_y = rows-2
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    # exit()
    
    return Barbarian_list

def spawn4(arr, Buildings, king1):
    clear()
    print('Your spawn point is present at (first row, last column)')
    arr[0][0] = '#'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Archer_Single = Archer()
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)  
    Archer_Single.arch_spawn(arr, 1, cols-2, Buildings, king1)
    Archer_list.append(Archer_Single)
    spawn_x = 1
    spawn_y = cols-2
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    return Archer_list

def spawn5(arr, Buildings, king1):
    clear()
    arr[0][0] = '#'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Archer_Single = Archer()
    Archer_Single.arch_spawn(arr, int(rows/2)-1, 1, Buildings, king1)
    Archer_list.append(Archer_Single)
    spawn_x = int(rows/2)-1
    spawn_y = 1
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
    return Archer_list

def spawn6(arr, Buildings, king1):
    clear()
    arr[1][1] = '.'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Archer_Single = Archer()
    Archer_Single.arch_spawn(arr, rows-2, cols-2, Buildings, king1)
    Archer_list.append(Archer_Single)
    spawn_x = rows - 2
    spawn_y = cols - 2
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    # exit()
    
    return Archer_list

def spawn7(arr, Buildings, king1):
    clear()
    print('Your spawn point is present at (first row, last column)')
    arr[0][0] = '#'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Balloon_Single = Balloon()
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)  
    Balloon_Single.balloon_spawn(arr, 1, int(cols/2)-1, Buildings, king1)
    Balloon_list.append(Balloon_Single)
    spawn_x = 1
    spawn_y = cols-2
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    return Balloon_list

def spawn8(arr, Buildings, king1):
    clear()
    arr[0][0] = '#'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Balloon_Single = Balloon()
    Balloon_Single.balloon_spawn(arr, int(rows/2)-1, cols - 2, Buildings, king1)
    Balloon_list.append(Balloon_Single)
    spawn_x = int(rows/2)-1
    spawn_y = cols - 2
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health)
    return Balloon_list

def spawn9(arr, Buildings, king1):
    clear()
    arr[1][1] = '.'
    arr[int(rows/2)][cols-1] = '#'
    arr[rows-1][int(cols/2)] = '#'
    Balloon_Single = Balloon()
    Balloon_Single.balloon_spawn(arr, 1, 3, Buildings, king1)
    Balloon_list.append(Balloon_Single)
    spawn_x = 1
    spawn_y = 3
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    if king1.health > 0:
        remaining = int(king1.health/20)
        health = '♥' * remaining
        print("Player's health: " +  health) 
    # exit()
    
    return Balloon_list


