from random import *
from time import sleep
from func_stats import *
from func_menu import *
switches = [0,1]
fightswitch = choice(switches)

#fight system
def villain():
  global fightswitch
  global hp
  global bonushp
  global enemyhp
  global run_value
  if fightswitch == 0:
        enemyattackrange = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
        ch = choice(enemyattackrange)
        hp=hp-ch+bonusshield
        print(spacer)
        print(f"Enemy attacked you! You lost {ch-bonusshield} hp!\n")
        sleep(1)
        print(spacer)
        fightswitch = 1

def hero():
  global fightswitch
  global hp
  global bonushp
  global enemyhp
  global run_value
  if fightswitch == 1:
    print(spacer)
    print(f"\nPlayer HP = {hp}\t\t\tEnemy HP = {enemyhp}\n")
    inp = int(input("-- FIGHT --\n1)Attack 2)Defend 3)Use consumables 4)Run Away\n: "))
    print(spacer)
    if inp == 4:
      run_value = 1
    elif inp == 3:
      if len(consumables)>0:
        print(spacer)
        print(f"You have {len(consumables)} items you can use!")
        print(f"You have opened the inventory! You have {len(consumables)} items!")
        print(f"potion x {consumables.count('potion')}",end = ', ')
        print(f"poison x {consumables.count('poison')}",end = ', ')
        print(f"berry x {consumables.count('berry')}",end = ', ')
        print(f"water x {consumables.count('water')}",end = ', ')
        print()
        print(spacer)
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
      else:
        print("You have no consumables you can use!")
        print(spacer)
        
    elif inp == 2:
      parryvalues = [0,10,20,30,40,50]
      e = choice(parryvalues)
      if hp+e<defaulthp+bonushp:
        hp+=e
        print(f"You parried and regained {e} hp")
        print(spacer)
        sleep(1)
      else:
        hp = defaulthp+bonushp
        print(f"You parried and regained all of your hp")
        print(spacer)
        sleep(1)
      fightswitch = 0
    elif inp == 1:
      attackvalues = [0,10,20,30,40,50]
      e = choice(attackvalues)
      if enemyhp-e>0:
        enemyhp-=e
        print(f"You attacked the enemy! Enemy lost {e} hp\n")
        print(spacer)
        sleep(1)
      else:
        enemyhp=0
        print(f"You attacked the enemy! Enemy lost all of their hp\n")
        sleep(1)
        print(spacer)
      fightswitch = 0


def randomencounter():
  global fightswitch
  global hp
  global bonushp
  global enemyhp
  global money
  global run_value
  encountered = choice(enemies)
  print(f"You have encountered {encountered}!")
  print(spacer)
  enemyhp=choice(randomnos)
  while enemyhp>0 or hp>0:
    if run_value == 1:
      print(f"You have escaped from {encountered}")
      run_value = 0
      print(spacer)
      sleep(1)
      break
    else:
      if fightswitch == 1:
        hero()
      elif fightswitch == 0:
        villain()
    if enemyhp <= 0:
      print(f"You have successfully defeated {encountered}")
      coingain = choice(randomnos)
      money+=coingain
      print(f"You gained {coingain} coins!")
      print(spacer)
      sleep(1)
      break
    elif hp <= 0:
      print(f"You have been killed by {encountered}")
      coinlose = choice(randomnos)
      if money-coinlose>0:
        money-=coinlose
        print(f"You lost {coinlose} coins!")
      else:
        money = 10
        hp = 1
        print("You managed to hold onto 10 coins and escape with 1 hp!")
        break
      print(spacer)
  


from random import *
from time import sleep
from func_stats import *


#event functions 
#random item pickup event
def item():
    global items
    itemlist = ['potion','poison','berry','water','nothing'] #note these are consumables not stat boosters
    pickedplace = ['lying near the wall','inside a cavity','on the ground','mysteriously in your pocket'
                   ,'with the help of the torch on the walls']
    picked = choice(itemlist)
    if picked != 'nothing':
        print(f"You found a {picked} {choice(pickedplace)}")
        consumables.append(picked)
        print(spacer)
    else:
        print("You found nothing")
        print(spacer)

#random hpgainlose event
def hp_():
    global hp
    global defaulthp
    global bonushp
    hplst = [1,2,3,4,5,6,7,8,9,10]
    hpgain = choice(hplst)
    hpch = ['gain','lose']
    chplaceadd = ['due to a magic scroll','from the fountain of life','from a gnome']
    chplacelose = ['due to tripping on a rock','from falling off a small cliff','from accidentally burning yourself']
    ch = choice(hpch)
    if ch == 'gain':
        if hp+hpgain<=defaulthp+bonushp:
            print(f"You Gained {hpgain} hp {choice(chplaceadd)}")
            print(spacer)
            hp = hp + hpgain
        else:
            print(f"You found a vial of {hpgain} hp but your hp is too full so you dropped it!")
            print(spacer)
    elif ch == 'lose':
        if hp-hpgain>=0:
            print(f"You Lost {hpgain} hp {choice(chplacelose)}")
            print(spacer)
            hp = hp - hpgain
        else:
            print(f"You should have lost {hpgain} hp {choice(chplacelose)} but you narrowly avoided it!")
            print(spacer)
          
          
#menu functions

#1
def randomiser():
    events = ['item','fight','hp','none']
    event =choice(events)
    if event == 'item':
        item()
    elif event == 'fight':
        randomencounter()
    elif event == 'hp':
        hp_()
    elif event == 'none':
        print('Nothing Happened')
        print(spacer)
        
      
#2 needs #1 to work   

def mover():
    print(spacer)
    x=int(input("Enter Grid Number to move []: "))
    print(spacer)
    if x>=1 and x<=9:
        print(grid_pos[x])
        print()
        sleep(1)
        randomiser()
    else:
        print("Out of bounds!")
        mover()

#3
def inventory():
    global hp
    print(spacer)
    print(f"You have opened the inventory! You have {len(consumables)} items!")
    print(f"potion x {consumables.count('potion')}",end = ', ')
    print(f"poison x {consumables.count('poison')}",end = ', ')
    print(f"berry x {consumables.count('berry')}",end = ', ')
    print(f"water x {consumables.count('water')}",end = ', ')
    print()
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
          if hp-30>0:
            hp-=30
            print("You drank poison and lost 30 HP!")
            print(spacer)
          else:
            hp = 1
            print("You are on the brink of death!")
            print(spacer)
    else:
      print("Item doesnt exist?!")
    print()
    sleep(1)
  
#4
def stats():
    print(spacer)
    print(f"HP = {hp}\nBonus HP = {bonushp}\nShield = {bonusshield}\nMoney = {money}")
    print(spacer)
  
#5 needs #2 #3 #4 to work
def menu():
    print(spacer)
    cho = int(input(f"--- 1)Move 2)Inventory 3)Stats ---\n{spacer}\n: "))
    if cho == 1:
        mover()
    elif cho == 2:
        inventory()
    elif cho == 3:
        stats()
    else:
        print("Invalid Choice")
        
