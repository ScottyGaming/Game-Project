from random import *
from time import sleep
from func_vars import *
from func_fight import *
from func_menu import *
from func_messages import _noitemfind,_randomitemfind,_genericnothing

#random item pickup event
def item():
    global consumabledict
    picked = choice(list(consumabledict))
    if picked != 'nothing':
        print(f"You found a {picked} {choice(_randomitemfind)}")
        consumables.append(picked)
    else:
        print(_noitemfind)
      
def invlist():
  print(f"You have opened the inventory! You have {len(consumables)} items!")
  print(f"potion x {consumables.count('potion')}",end = ', ')
  print(f"poison x {consumables.count('poison')}",end = ', ')
  print(f"berry x {consumables.count('berry')}",end = ', ')
  print(f"water x {consumables.count('water')}",end = ', ')
  print()
  
def nothing():
  print(_genericnothing)