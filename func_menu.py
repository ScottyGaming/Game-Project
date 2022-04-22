from random import *
from time import sleep
from func_vars import *
from func_events import *
from func_fight import *
from func_graphics import grid_pos

#menu functions

#1
def randomiser():
  e = ['item','nothing','encounter']
  eeee = choice(e)
  if eeee == "item":
    item()
  elif eeee == 'nothing':
    nothing()
  elif eeee == 'encounter':
    encounter()
           
#2 needs #1 to work   
def mover():
  x=int(input("Enter Grid Number to move []: "))
  if x>=1 and x<=gridno:
    print(f"\n{grid_pos[x]}\n")
    randomiser()
  else:
    print("You tried to go to out of bounds!")

#3
def inventory():
    invlist()

#4
def stats():
  print(f"HP = {maxpossiblehp}\nMoney = {sum(money)}")
    
  
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
        
