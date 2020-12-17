# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
swap=0
noswap=0
total=0
ch='y'
while ch=='y':
    gates=[0]*3
    goats=[]
    x=random.randint(0,2)
    gates[x]="car"
    for i in range(3):
        if i==x:
            continue
        else:
            gates [i] ="Goat"
            goats.append(i)
    choice=int(input("Select a lucky Gate for you among 0,1,2 : \t"))
    door_open=random.choice(goats)
    while door_open==choice:
        door_open=random.choice(goats)
    print("Opening a Door for You and that is gate no. " +str(door_open))
    mind=input("u want to change your previous choice, then press y for yes or press n for no \t")
    if mind=="y":
        swap=swap+1
        if gates[choice]=="Goat":
            print("congrats You are the winner !!\n")
            print("you won the vittara !!")
        else:
            print(" You lost better luck next time!!\n")
            print("But not to worry it wasn't last chance !!")
    else:
        noswap=noswap+1
        if gates[choice]=="Goat":
            print(" You lost better luck next time !!\n")
            print("But not to worry it wasn't last chance !!")
        else:
            print(" You are the winner !!\n")
            print("you won the vittara !!")
            
    total=total+1
    ch=input("Wanna play more,then press y for yes or n for no !! : ")
    print("Winning stats : " +str(swap)+ " when you swap ")
    print("Winning stats : " +str(noswap)+ " when you don't swap ")
    print("Total match played : ",total)

