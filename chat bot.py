# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:40:22 2020

@author: rk239
"""
#description this is a chat bot program
#import the library 
#if you want to quit this you want to type quit

from nltk.chat.util import Chat,reflections
pairs=[
       ['my name is (.*)',['hi %1']],
       ['(hi|hello|hey|holla|hola)',['hey there','hi there']],
       ['(fee|addmission)',['which course']],
       ['(Bca|Bba|Mba|Msc it)' ,['there has an  two types- national and international']],
       
      
       ['((.*) created you?)',[" ritik kumar created me by using pyhton"]], 
       ['((.*) your developer?)',[" ritik kumar developed me by using python "]],
       ['(.*) help ',['yes ,i can help you.']],
       ['(.*) your name ?',['my name is R.K.S.I.N.G.H']],
       ['thanxs',['welcome ,thanxs for using me.']],
       ['(about college|further details)',['visit our official site www.icasr.org'] ],
      
       ]



Chat=Chat(pairs,reflections)

Chat.converse()
