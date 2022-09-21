# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:51:20 2022

@author: Gunjan
"""


from PIL import Image
import random 
end=100

def check_ladder(points):
    if points==2:
        print('Ladder ')
        return 23
    elif points==6:
        print('LADDER ')
        return 45
    elif points==20:
        print('LADDER ')
        return 59
    elif points==57:
        print('LADDER ')
        return 96
    elif points==52:
        print('LADDER ')
        return 72
    elif points==71:
        print('LADDER ')
        return 92
    else:
        return points
    
def check_snake(points):
    if points==50:
        print("SNAKE")
        return 5
    elif points==43:
        print("SNAKE")
        return 17
    elif points==56:
        print("SNAKE")
        return 8
    elif points==73:
        print("SNAKE")
        return 15
    elif points==84:
        print("SNAKE")
        return 63
    elif points==87:
        print("SNAKE")
        return 49
    elif points==98:
        print("SNAKE")
        return 40
    else:
        return points

def show_board():
    img=Image.open("snl.jpg")
    img.show()
def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    p1_name=input(' Player 1, please enter your name')
    p2_name=input(' Player 2, please enter your name')
    pp1=0
    pp2=0
    
    turn=0
    while(1):
        if turn%2==0:
            print(p1_name,'YOUR turn ')
            c=input('Press 1 to continue, 0 to quit ')
            if c==0:
                print(p1_name, 'scored ',pp1)
                print(p2_name, 'scored ',pp2)
                print('Quitting the game, Thanks for playing ')
                break
            
            
            dice = random.randint(1,6)
            print(" dice showed ",dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=end
            print(p1_name,' Your score ',pp1)
            if(reached_end(pp1)):
                print(p1_name,' won')
                break
        else:
            print(p2_name,'YOUR turn ')
            c=input('Press 1 to continue, 0 to quit ')
            if c==0:
                print(p1_name, 'scored ',pp1)
                print(p2_name, 'scored ',pp2)
                print('Quitting the game, Thanks for playing ')
                break
            
            
            dice = random.randint(1,6)
            print(" dice showed ",dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                pp2=end
            print(p2_name,' Your score ',pp2)
            if(reached_end(pp2)):
                print(p2_name,' won')
                break
            
        turn = turn +1 
show_board()
play()
