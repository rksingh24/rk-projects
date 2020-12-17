# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:53:06 2020

@author: Ritik
"""


def welcome():
    print("\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609 \U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609")
    print("  w      w       w   eeeee  ll    ll     ccccc  ooooo  mm   mm  eeeee                     !")
    print("   w    w  w    w    e      ll    ll     c      o   o  m m m m  e                         !")
    print("    w  w    w  w     eeeee  ll    ll     c      o   o  m  m  m  eeeee                     !")
    print("     w       w       e      ll    ll     c      o   o  m     m  e                         !")
    print("     w       w       eeeee  lllll lllll  ccccc  ooooo  m     m  eeeee                     !")
    print("__________________________________________________________________________________________!")
    print("         ||||||            ttttt h     eeee       GGGG      AAAA  MM   MM  EEEEE          !")
    print("           |    o o o        t   h     e          G         A  A  M M M M  E              !")
    print("           |    o   o        t   hhhh  eeeee      G         AAAA  M  M  M  EEEEE          !")
    print("           |    o o o        t   h  h  e          G  GGGGG  A  A  M     M  E              !")
    print("                             t   h  h  eeeee      GGGGG  G  A  A  M     M  EEEEE          !")
    print("__________________________________________________________________________________________!\n")
    print("\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609")

def instruction():
    print("__________________________________________________________________________")
    #this  print line copy toh google import randintek of geek -
    print(" Winning Rules of the Rock paper scissor game as follows: \n"
                                +"\n Rock vs paper->paper wins  \n"
                                + "\n Rock vs scissor->Rock wins  \n"
                                +"\nPaper vs scissor->scissor wins \ \n")
    print("\U0001F609 GAME IS LOADING......\n") 
    print("__________________________________________________________________________\n")
def exit():
    print("\n")
    print("!___________________________________________________________________________")
    print("\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609")
    print("!___________________________________________________________________________")
    print("\U0001F642              Thanxs for playing                                    \U0001F642 ")
    print("!___________________________________________________________________________")
    print("\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609\U0001F609")
    print("!___________________________________________________________________________\n")




# import emoji module  
import emoji 
import random 
welcome()

instruction()


print("------------------------------------------------------")
print("\nYou want to play with computer press=1 :\n"
                 +" u want to play with  2 player press=2:\n")
print("------------------------------------------------------")
choice=int(input(" choice:--"))
if choice==1:
    
#player use for  store name
    player=input("Enter your name---")




#B used for store the choice of player 
    B= input(" For player :Rock(R), Paper(P) or Scissors(S):---")
    A = ["R", "P", "S"]
 #in randint  0=starting and 2 is ending poinT:
    computer = A[random.randint(0, 2)]
 #logic for the game and comparison
    if B == computer:
    
         print("***DRAW  ")
         print(emoji.emojize(":winking_face_with_tongue:")) 
    elif ( B == "R" and computer == "S")or(B == "S" and computer == "P")or(B == "P" and computer == "R"):
             # grinning squinting face
             print(player," You Win the game  \U0001F606 \U0001F606")
    elif  (B == "P" and computer == "R")or( B == "R" and computer == "S")or(B == "S" and computer == "P"):
        
        print(" computer win the game ")
            # rolling on the floor laughing 
        print("\U0001F923  ") 
#if player enter wrong choice the else statement  occurs
    else:
             # grinning face 
        print(" ERROR:ENTER only ONE of them R,P,S: \U0001f600 ")
            
        
#this is for 2 player game
else:
    print("----------------------------")
    #player use for  store name
    player1=input("Enter your name---  ")
    player2=input(" Enter your name--- ")
    print("----------------------------")


   
#B used for store the choice of player 
    print("------------------------------------------------------------------")
    B= input(" For player 1 : Rock(R), Paper(P) or Scissors(S):---")
    C= input(" For  player 2:Rock(R), Paper(P) or Scissors(S):---")
    print("------------------------------------------------------------------")
 #logic for the game and comparison
    if B == C:
        print(" Draw ")
        print(emoji.emojize(":winking_face_with_tongue:")) 
    elif( B == "R" and C == "P")or (B == "S" and C == "P")or( B == "R" and C == "S"):
            # grinning face 
        print(player1," You Win the game \U0001f600 \U0001f600")
    elif( C == "P" and B == "R")or( C == "R" and B == "S")or( C == "S" and B == "P"):
        
            # grinning squinting face
        print(player2,"Win the game \U0001F606  \U0001F606")
#if player enter wrong choice the else statement  occurs
    else:
        
        print("***ERROR:Enter only one of them R,P,S: ")
            # rolling on the floor laughing 
        print("\U0001F923") 
    

exit()

