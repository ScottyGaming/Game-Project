from func_events import *
from func_graphics import *
from func_menu import *
from func_messages import *
from func_vars import *
from random import *

#switches
run_switch = 0
fightswitches = [0,1];fight_switch = choice(fightswitches)


#counters
enemies_defeated = 0
bosses_defeated = 0

#loot_tables
Enemies = {0:0,('Slime','Goblin','Imp','Cougar'):[50,10,10]
,('Rogue','Bat','Smurf','Zombie'):[80,20,20]
,('Skeleton','Golem','Troll','Kobold'):[100,20,30]
,('Giant','Great Unclean','Tyranid','Orc','Necron'):[200,50,40]
,('Fallen Palladin','Druid','Doraemon'):[300,100,50]}
enemies = list(Enemies.keys())
loot = list(Enemies.values())

money = [100]
#Enemies:hp,xp,coins

def villain():
  global hp
  global fight_switch
  ch = choice(attackrange)
  hp=hp-ch
  print(f"Enemy attacked you! You lost {ch} hp!\n")
  sleep(1)
  fight_switch = 1

def hero():
  global hp
  global fight_switch
  global enemyhp
  print(f"\nPlayer HP = {hp}\t\t\tEnemy HP = {enemyhp}\n")
  inp = int(input("-- FIGHT --\n1)Attack 2)Defend 3)Use consumables 4)Run Away\n: "))
  if inp == 4:
          run_switch = 1
          
  elif inp == 3:
          if len(consumables)>0:
            invlist()
            useitemduringfight()
          else:
            print("You have no consumables you can use!")
            
  elif inp == 2:
          parryvalues = [0,10,20,30,40,50]
          e = choice(parryvalues)
          if hp+e<maxpossiblehp:
            hp+=e
            print(f"You parried and regained {e} hp")
            sleep(1)
          else:
            hp = maxpossiblehp
            print(f"You parried and regained all of your hp")
            sleep(1)
          
  elif inp == 1:
          e = choice(attackrange)
          if enemyhp-e>0:
            enemyhp-=e
            print(f"You attacked the enemy! Enemy lost {e} hp\n")
            sleep(1)
          else:
            enemyhp=0
            print(f"You attacked the enemy! Enemy lost all of their hp\n")
            sleep(1)
  fight_switch = 0

def encounter():
  global hp
  global enemyhp
  global fight_switch
  global money
  index = choice([1,2,3,4,5])
  enemy = choice(enemies[index])
  enemyhp = loot[index][0]
  xp = loot[index][1]
  coin = loot[index][2]
  print(f"You have encountered {enemy} with {enemyhp} hp!")

  while hp>0 or enemyhp>0:
    global run_switch
    if run_switch == 0:
      if fight_switch == 0:
        villain()
  
      elif fight_switch == 1:
        hero()
        
    else:
      print(f"You have escaped from {enemy}")
      break
      
    if enemyhp <= 0:
        print(f"You have successfully defeated {enemy}")
        coingain = coin
        money.append(coingain)
        print(f"You gained {coingain} coins!")
        sleep(1)
        break
    elif hp <= 0:
        print(f"You have been killed by {enemy}")
        coinlose = choice(randomnos)
        money.append(-coinlose)
        print(f"You lost {coinlose} coins!")
        hp = choice([10,20,30,40,50,60])
        print(f"You were slain by {enemy} ! Barely holding onto life you escape!")
        break

      
    