from random import *
from time import sleep
from func_vars import *
from func_menu import *


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
        invlist()
        useitemduringfight()
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

  