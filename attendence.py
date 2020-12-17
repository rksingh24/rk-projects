# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:30:41 2020

@author: rk239
"""
import datetime


def attendence():
    s=open("bca_attendence.txt","a+")
    
    
    print("A=ABSENT \n P=PRESENT")
    
    
    date = datetime.datetime.today()
    prof=input("Enter proffesor  name -")
    sub=input("Enter subject name-")
    Deepak=input("   Deepak       ----")
    Ritik=input("    Ritik        ----")
    Jaya=input("     Jaya         ----")
    Anjana=input("   Anjana       ----")
    Kinjalika=input("Kinjalika      ----")
    Utpal=input("    Utpal         ----")
    Bhagyesh=input(" Bhagyesh      ----")
    Rakesh =input("  Rakesh         ----")
    Taushif=input("  Taushif       ----")
    Rashid=input("   Rashid        ----")
    Mehmood=input("  Mehmood       ----")
    Abhiuday=input(" Abhiuday        ----")
    Kaushal=input("  Kaushal        ----")
    Kartik=input("   Kartik         ----")
    
    
    
    
    print(date)
    print("\nATTENDENCE LIST") 
    print("Deepak      --",Deepak)
    print("Ritik       --",Ritik)
    print("Jaya        --",Jaya)
    print("Anjana      --",Anjana)
    print("Kinjalika   --",Kinjalika)
    print("Utpal       --",Utpal)
    print("Bhagyesh    --",Bhagyesh)
    print("Rakesh      --",Rakesh)
    print("Taushif     --", Taushif)
    print("Rashid      --",Rashid)
    print("Mehmood     --",Mehmood)
    print("Abhiuday    --",Abhiuday)
    print("Kaushal     --",Kaushal)
    print("Kartik      --",Kartik)
    
    a=str(date)
    s.write("\n------------------------------------------------------------------------------\n")
    s.write("Date=="+str(a))
    s.write("\n------------------------------------------------------------------------------\n")
    s.write("\n   BACHELOR'S OF COMPUTER APPLICATION  \n")
    s.write("\n------------------------------------------------------------------------------\n")
    s.write("\n Prof ===>>"+str(prof))
    s.write("\n------------------------------------------------------------------------------\n")
    s.write("\n sub ===>>"+str(sub))
    s.write("\n------------------------------------------------------------------------------\n")
    s.write("         ATTENDENCE SHEET   \n")
    s.write("\n------------------------------------------------------------------------------\n")
    s.write("\n | Deepak    |"+str(Deepak)   +"|")
    s.write("\n | Ritik     |"+str(Ritik)    +"|")
    s.write("\n | Jaya      |"+str(Jaya)     +"|")
    s.write("\n | Anjana    |"+str(Anjana)   +"|")
    s.write("\n | Kinjalika |"+str(Kinjalika)+"|")
    s.write("\n | Utpal     |"+str(Utpal)    +"|")
    s.write("\n | Bhagyesh  |"+str(Bhagyesh) +"|")
    s.write("\n | Rakesh    |"+str(Rakesh)   +"|")
    s.write("\n | Taushif   |"+str(Taushif)  +"|")
    s.write("\n | Rashid    |"+str(Rashid)   +"|")
    s.write("\n | Mehmood   |"+str(Mehmood)  +"|")
    s.write("\n | Abhiuday  |"+str(Abhiuday) +"|")
    s.write("\n | Kaushal   |"+str(Kaushal)  +"|")
    s.write("\n | Kartik    |"+str(Kartik)   +"|")
    s.write("\n------------------------------------------------------------------------------\n")
    s.write("\n------------------------------------------------------------------------------\n")
    s.close()
    
attendence()    
    
    