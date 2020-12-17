# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:28:03 2020

@author: Ritik
"""



import random

for i in range(7)    :
    a=int(input("chosee a number between 1 to 10--"))
    account=100
    
    win=0
    loose=0
    c=random.randint(1, 10) 
    if c==a:
        print(c)
        print("you  win lottery")
        account=account+1000-100
        win=win+1
    else:
        print(c)
        print("you losse")
        account=account-100
        loose=loose+1
    print(win,"you win" )
    print(loose,"you loose")
    print(account,"balance")
