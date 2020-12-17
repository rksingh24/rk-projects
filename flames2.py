# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:05:46 2020

@author: Ritik
"""

name = input('Enter your 1st name: ')

name1 = input('Enter your crush name: ')

print(name)
print(name1)

for i in name:
    for j in name1:
        if i==j:
            
           name=name.replace(i,"",1)
           name1=name1.replace(j,"",1)
           break
       
count= len (name+name1)
print(count)

if count>0:
  flames=["friends","lovers","affection","marriage","Enemy","sister"]
  while len(flames)>1:
      c = count % len (flames)
      length = c-1
      if length>=0:
          left = flames[:length]
          right = flames[length+1:]
          flames = right+left
      else:
              flames=flames[:len(flames)-1]
  print("Relation with your crush is:",flames[0])
else:
  print("enter different names")