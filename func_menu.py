from random import *
from time import sleep
from func_vars import *
from func_fight import *
from func_events import *
from func_graphics import grid_pos
from func_messages import _outofbounds,_completeheal
#menu functions

#1
def randomiser():
  choice([item,randomencounter,nothing])()

#2 needs #1 to work   
def mover():
    x=int(input("Enter Grid Number to move []: "))
    if x>=1 and x<=gridno:
        print("\n",grid_pos[x],"\n")
        randomiser()
    else:
      print(_outofbounds)
      mover()

#3
def inventory():
    invlist()
    global hp
    inp = input("Enter name of item you want to use: ")
    if inp in consumables and inp == 'potion':
          if hp+50 <= maxpossiblehp:
            hp+=50
            print("You have regained 50 HP!")
            
          else:
            hp=maxpossiblehp
            print(_completeheal)
            
    elif inp in consumables and inp == "berry":
          if hp+20 <= maxpossiblehp:
            hp+=20
            print("You have regained 20 HP!")
            
          else:
            hp=maxpossiblehp
            print(_completeheal)
            
    elif inp in consumables and inp == "water":
          if hp+10 <= maxpossiblehp:
            hp+=10
            print("You have regained 10 HP!")
            
          else:
            hp=maxpossiblehp
            print(_completeheal)
            
    elif inp in consumables and inp == "poison":
          if hp-30>0:
            hp-=30
            print("You drank poison and lost 30 HP!")
            
          else:
            hp = 1
            print("You are on the brink of death!")
            
    else:
      print("Item doesnt exist?!")
    print()
    sleep(1)
  
#4
def stats():
  print(f"HP = {hp}\nBonus HP = {bonushp}\nShield = {shield}\nBonus Shield = {bonusshield}\nMoney = {money}")
    
  
#5 needs #2 #3 #4 to work
def menu():
    
    cho = int(input(f"--- 1)Move 2)Inventory 3)Stats ---\n: "))
    if cho == 1:
        mover()
    elif cho == 2:
        inventory()
    elif cho == 3:
        stats()
    else:
        print("Invalid Choice")
        
