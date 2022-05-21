# -*- coding: utf-8 -*-
from pickle import FALSE, TRUE
from os import system
import os
import json
from colorama import Fore, Back, Style
# import config as C
from os.path import exists
from src.building import *
from src.input import *
from src.king import *
from src.barbarians import *
from src.archers import *
from src.commands import *
from src.commandking import *
import random
import time

rows = 30
cols = 60

frames = 0
harshit = []

def play(level):
    counter = 0
    arr = [[
        "\033[36m" + '.' + "\033[36m" for i in range(cols)] for j in range(rows)]

    king1 = king()
    king2 = king()
    replaymode = FALSE
    Instructions = []

    def init_board():
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    arr[i][j] = '#'
                else:
                    arr[i][j] = '.'


    init_board()


    def clear():
        _ = system('clear')

    Town_Hall = Building(4, 3, 'Town Hall', 'H')
    Cannon1 = Defense(3, 3, 'Cannon', 'C')
    Cannon2 = Defense(3, 3, 'Cannon', 'C')
    Hut1 = Building(4, 2, 'Hut', 'H')
    Hut2 = Building(4, 2, 'Hut', 'H')
    Hut3 = Building(4, 2, 'Hut', 'H')
    Hut4 = Building(4, 2, 'Hut', 'H')
    Hut5 = Building(4, 2, 'Hut', 'H')
    Wizard1 = Wizard(1, 1, 'Wizard', 'M')
    Wizard2 = Wizard(1, 1, 'Wizard', 'M')

    if level == 2 or level == 3:
        Cannon3 = Defense(3, 3, 'Cannon', 'C')
        Wizard3 = Wizard(1, 1, 'Wizard', 'M')
    
    if level == 3:
        Cannon4 = Defense(3, 3, 'Cannon', 'C')
        Wizard4 = Wizard(1, 1, 'Wizard', 'M')
    king1.x_coord = 15
    king1.y_coord = 1
    Barbarian_list = []
    Archer_list = []
    Balloon_list = []
    clear()
    if level == 1:
        print(
            '''
██╗   ██╗██╗   ██╗██████╗ ██████╗ ██╗  ██╗        ████████╗██╗  ██╗███████╗    ██╗███╗   ██╗ ██████╗███████╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
╚██╗ ██╔╝██║   ██║██╔══██╗██╔══██╗██║  ██║ ██╗    ╚══██╔══╝██║  ██║██╔════╝    ██║████╗  ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
 ╚████╔╝ ██║   ██║██║  ██║██║  ██║███████║ ╚═╝       ██║   ███████║█████╗      ██║██╔██╗ ██║██║     █████╗  ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║  ██║██║  ██║██╔══██║ ██╗       ██║   ██╔══██║██╔══╝      ██║██║╚██╗██║██║     ██╔══╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
   ██║   ╚██████╔╝██████╔╝██████╔╝██║  ██║ ╚═╝       ██║   ██║  ██║███████╗    ██║██║ ╚████║╚██████╗███████╗██║        ██║   ██║╚██████╔╝██║ ╚████║
   ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝           ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                                                                
            '''
        )

        print(
            '''
            ██╗     ███████╗██╗   ██╗███████╗██╗          ██╗
            ██║     ██╔════╝██║   ██║██╔════╝██║         ███║
            ██║     █████╗  ██║   ██║█████╗  ██║         ╚██║
            ██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║          ██║
            ███████╗███████╗ ╚████╔╝ ███████╗███████╗     ██║
            ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝     ╚═╝

            '''
        )

    if level == 2:
        print(
            '''
            ██╗     ███████╗██╗   ██╗███████╗██╗         ██████╗ 
            ██║     ██╔════╝██║   ██║██╔════╝██║         ╚════██╗
            ██║     █████╗  ██║   ██║█████╗  ██║          █████╔╝
            ██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║         ██╔═══╝ 
            ███████╗███████╗ ╚████╔╝ ███████╗███████╗    ███████╗
            ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝    ╚══════╝
                                                     
            '''
        )

    if level == 3:
        print(
            '''  
            ██╗     ███████╗██╗   ██╗███████╗██╗         ██████╗ 
            ██║     ██╔════╝██║   ██║██╔════╝██║         ╚════██╗
            ██║     █████╗  ██║   ██║█████╗  ██║          █████╔╝
            ██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║          ╚═══██╗
            ███████╗███████╗ ╚████╔╝ ███████╗███████╗    ██████╔╝
            ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝    ╚═════╝ 
                                                                                         
            '''
        )
    print('\n'.join(map(lambda b: ''.join(map(str, b)), arr)))
    print("Choose character: K for King and Q for Archer Queen")
    symbol = input()
    harshit.append(symbol)
    print("To start the game, press any number key to start - each corresponds to a different spawn point and a different troop")
    print("Barbarians: 1, 2, 3")
    print("Archers: 4, 5, 6")
    print("Balloons: 7, 8, 9")
    system('aplay -q music/poc.wav&')
    king1.symbol = symbol
    arr[king1.x_coord][king1.y_coord] = "\033[32m" + symbol + "\033[0m"

    Town_Hall.draw(12, 28, arr)
    Cannon1.draw(12, 14, arr)
    Cannon2.draw(12, 43, arr)
    Hut1.draw(4, 12, arr)
    Hut2.draw(4, 27, arr)
    Hut3.draw(4, 42, arr)
    Hut4.draw(16, 18, arr)
    Hut5.draw(16, 37, arr)
    Wizard1.draw(20, 22, arr)
    Wizard2.draw(20, 35, arr)
    if level == 2:
        Cannon3.draw(22, 28, arr)
        Wizard3.draw(26, 29, arr)
    if level == 3:
        Cannon3.draw(22, 14, arr)
        Wizard3.draw(26, 22, arr)
        Cannon4.draw(22, 43, arr)
        Wizard4.draw(26, 35, arr)

    Buildings = {}
    All_Buildings = {}
    for i in Town_Hall.points:
        Buildings[i] = Town_Hall
    for i in Cannon1.points:
        Buildings[i] = Cannon1
    for i in Cannon2.points:
        Buildings[i] = Cannon2
    for i in Hut1.points:
        Buildings[i] = Hut1
    for i in Hut2.points:
        Buildings[i] = Hut2
    for i in Hut3.points:
        Buildings[i] = Hut3
    for i in Hut4.points:
        Buildings[i] = Hut4
    for i in Hut5.points:
        Buildings[i] = Hut5
    for i in Wizard1.points:
        Buildings[i] = Wizard1
    for i in Wizard2.points:
        Buildings[i] = Wizard2
    if level == 2:
        for i in Cannon3.points:
            Buildings[i] = Cannon3
        for i in Wizard3.points:
            Buildings[i] = Wizard3
    if level == 3:
        for i in Cannon3.points:
            Buildings[i] = Cannon3
        for i in Wizard3.points:
            Buildings[i] = Wizard3
        for i in Cannon4.points:
            Buildings[i] = Cannon4
        for i in Wizard4.points:
            Buildings[i] = Wizard4

    All_Buildings = Buildings

    for i in range(10, 18, 1):
        for j in range(26, 33, 1):
            if i == 10 or i == 17 or j == 26 or j == 32:
                Wall_single = Wall(1, 1, 'Wall', 'W')
                Wall_single.draw(i, j, arr)
                Buildings[(i, j)] = Wall_single

    while(Buildings):
        command = input_to(Get(), 1)
        if command != '0':
            Instructions.append(command)
        if command == '0':
            print ('''

            ███████╗██╗  ██╗██╗████████╗███████╗██████╗         ██████╗ ██████╗ ██╗    ██╗ █████╗ ██████╗ ██████╗ 
            ██╔════╝╚██╗██╔╝██║╚══██╔══╝██╔════╝██╔══██╗       ██╔════╝██╔═══██╗██║    ██║██╔══██╗██╔══██╗██╔══██╗
            █████╗   ╚███╔╝ ██║   ██║   █████╗  ██║  ██║       ██║     ██║   ██║██║ █╗ ██║███████║██████╔╝██║  ██║
            ██╔══╝   ██╔██╗ ██║   ██║   ██╔══╝  ██║  ██║       ██║     ██║   ██║██║███╗██║██╔══██║██╔══██╗██║  ██║
            ███████╗██╔╝ ██╗██║   ██║   ███████╗██████╔╝▄█╗    ╚██████╗╚██████╔╝╚███╔███╔╝██║  ██║██║  ██║██████╔╝
            ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═════╝ ╚═╝     ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 

            ''')
            if not os.path.isfile('replay/replay.json'):
                with open('replay/replay.json', 'w') as f:
                    json.dump(harshit, f)
            else:
                with open("replay/replay.json", "r+") as file:
                    data = json.load(file)
                    data.append(harshit)
                    file.seek(0)
                    json.dump(data, file)
            exit()     
        if command == '1':
            if len(Barbarian_list) > 5:
                continue
            Barbarian_list = spawn1(arr, Buildings, king1)
        if command == '2':
            if len(Barbarian_list) > 5:
                continue
            Barbarian_list = spawn2(arr, Buildings, king1)
        if command == '3':
            if len(Barbarian_list) > 5:
                continue
            Barbarian_list = spawn3(arr, Buildings, king1)   
        if command == '4':
            if len(Archer_list) > 5:
                continue
            Archer_list = spawn4(arr, Buildings, king1)
        if command == '5':
            if len(Archer_list) > 5:
                continue
            Archer_list = spawn5(arr, Buildings, king1)
        if command == '6':
            if len(Archer_list) > 5:
                continue
            Archer_list = spawn6(arr, Buildings, king1)
        if command == '7':
            if len(Balloon_list) > 5:
                continue
            Balloon_list = spawn7(arr, Buildings, king1)
        if command == '8':
            if len(Balloon_list) > 5:
                continue
            Balloon_list = spawn8(arr, Buildings, king1)
        if command == '9':
            if len(Balloon_list) > 5:
                continue
            Balloon_list = spawn9(arr, Buildings, king1)
        if command == 'w':
            movew(arr, All_Buildings, king1)
        if command == 's':
            moves(arr, All_Buildings, king1)
        if command == 'a':
            movea(arr, All_Buildings, king1)
        if command == 'd':
            moved(arr, All_Buildings, king1)
        if command == 'r':
            king1.rage()
        if command == 'h':
            king1.heal(Barbarian_list)
        if command == ' ':
            kingattack(arr, All_Buildings, king1)
        if command == 'x':
            axe(arr, All_Buildings, king1)
        if command == 'e':
            eagle(arr, All_Buildings, king1)
        for i in Barbarian_list:
            if Buildings:
                # print(Buildings)
                i.barb_move(arr, Buildings, king1)
                counter = 0
                for a in Buildings:
                    if Buildings[a].name == 'Wall':
                        counter += 1
                if counter == len(Buildings):
                    Buildings = {}
                    counter = 0
                    harshit.append(command)
                    break
        for i in Archer_list:
            if Buildings:
                # print(Buildings)
                i.arch_move(arr, Buildings, king1)
                counter2 = 0
                for a in Buildings:
                    if Buildings[a].name == 'Wall':
                        counter2 += 1
                if counter2 == len(Buildings):
                    Buildings = {}
                    counter = 0
                    harshit.append(command)
                    break
        for i in Balloon_list:
            if Buildings:
                # print(Buildings)
                # input()
                i.balloon_move(arr, Buildings, king1)
                counter2 = 0
                for a in Buildings:
                    if Buildings[a].name == 'Wall':
                        counter2 += 1
                if counter2 == len(Buildings):
                    Buildings = {}
                    counter = 0
                    harshit.append(command)
                    break

        Cannon_list = []
        Cannon_list = Barbarian_list + Archer_list
        Cannon1_result = Cannon1.attack(arr, Cannon_list, Barbarian_list, Archer_list, king1)
        Cannon_list = Cannon1_result[0]
        Barbarian_list = Cannon1_result[1]
        Archer_list = Cannon1_result[2]

        Cannon2_result = Cannon2.attack(arr, Cannon_list, Barbarian_list, Archer_list, king1)
        Cannon_list = Cannon2_result[0]
        Barbarian_list = Cannon2_result[1]
        Archer_list = Cannon2_result[2]

        Wizard_list = []
        Wizard_list = Barbarian_list + Archer_list + Balloon_list
        Wizard1_result = Wizard1.attack(arr, Wizard_list, Barbarian_list, Archer_list, Balloon_list, king1)
        Wizard_list = Wizard1_result[0]
        Barbarian_list = Wizard1_result[1]
        Archer_list = Wizard1_result[2]
        Balloon_list = Wizard1_result[3]

        Wizard2_result = Wizard2.attack(arr, Wizard_list, Barbarian_list, Archer_list, Balloon_list, king1)
        Wizard_list = Wizard2_result[0]
        Barbarian_list = Wizard2_result[1]
        Archer_list = Wizard2_result[2]
        Balloon_list = Wizard2_result[3]

        # print(type(Cannon1_result))
        # print(type(Wizard1_result))
        # print(Cannon_list)
        # print(Wizard_list)
        # print(Barbarian_list)
        # print(Archer_list)
        # print(Balloon_list)
        # print(Buildings)
        # print(king1.destroyed)
        # print("")
        # print(Cannon_list + Wizard_list)
        # input()
        if (Cannon_list + Wizard_list) == [] and king1.destroyed == TRUE:
            harshit.append(command)
            break
        
        # frames += 1
        # print(command)
        harshit.append(command)

    if(Buildings):
        print ('''

        ███████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗██╗
        ██╔════╝██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝██║
        ███████╗██║   ██║██████╔╝██████╔╝ ╚████╔╝      ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ██║
        ╚════██║██║   ██║██╔══██╗██╔══██╗  ╚██╔╝        ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ╚═╝
        ███████║╚██████╔╝██║  ██║██║  ██║   ██║▄█╗       ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗██╗
        ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝╚═╝       ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝

        ''')
        if not os.path.isfile('replay/replay.json'):
            with open('replay/replay.json', 'w') as f:
                json.dump(harshit, f)
        else:
            with open("replay/replay.json", "r+") as file:
                data = json.load(file)
                data.append(harshit)
                file.seek(0)
                json.dump(data, file)
                exit()
        
    else:
        print ('''

         ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗       ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗
        ██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝       ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║
        ██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗        ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║
        ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║         ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝
        ╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║▄█╗       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
        ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝

        ''')
        
        if level < 3:
            play(level + 1)
        elif level == 3:
            if not os.path.isfile('replay/replay.json'):
                with open('replay/replay.json', 'w') as f:
                    json.dump(harshit, f)
            else:
                with open("replay/replay.json", "r+") as file:
                    data = json.load(file)
                    data.append(harshit)
                    file.seek(0)
                    json.dump(data, file)
            exit()

play(1)
