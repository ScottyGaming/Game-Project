from random import *
from time import sleep
from func_vars import *
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

def useitemduringfight():
  global hp
  inp = input("Enter name of item you want to use: ")
  if inp in consumables and inp == 'potion':
          if hp+50 <= defaulthp+bonushp:
            hp+=50
            print("You have regained 50 HP!")
            print(spacer)
          else:
            hp=defaulthp+bonushp
            print("You have been healed completely")
            print(spacer)
  elif inp in consumables and inp == "berry":
          if hp+20 <= defaulthp+bonushp:
            hp+=20
            print("You have regained 20 HP!")
            print(spacer)
          else:
            hp=defaulthp+bonushp
            print("You have been healed completely")
            print(spacer)
  elif inp in consumables and inp == "water":
          if hp+10 <= defaulthp+bonushp:
            hp+=10
            print("You have regained 10 HP!")
            print(spacer)
          else:
            hp=defaulthp+bonushp
            print("You have been healed completely")
            print(spacer)
  elif inp in consumables and inp == "poison":
          if enemyhp-30 >= 0:
            enemyhp-=30
            print("Enemy Lost 30 HP!")
            print(spacer)
  else:
            enemyhp = 1
            print("Enemy is on the brink of death!")
            print(spacer)
  fightswitch = 0

def nothing():
  print(_genericnothing)