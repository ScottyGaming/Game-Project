from random import *

#defaultvars_hp
hp = 150
defaulthp = 150
bonushp = 0

#defaultvars_shield
defaultshield = 0
shield = 0
bonusshield = 0

#defaultvars_attack
defaultattach = 0
attack = 0
bonusattack = 0

#enemyhp
enemyhp = 100


#inventory
consumables = []
helditems = []
money = 100

#vars
randomnos=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
enemies = ['Troll','Slime','Demon','Goblin','Subs','The Creator G','Dragon','Griffin']
spacer = ""

#consumables
consumabledict = {'potion':50,'berry':20,'water':10,'nothing':'nothing'}
battleconsumablesdict = {'poison':30}

#triggers
run_value = 0
fightswitches = [0,1];fightswitch = choice(fightswitches)
gridno = 9
#checks
maxpossiblehp = defaulthp+bonushp