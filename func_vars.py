from random import *

#defaultvars_hp
hp = 150
defaulthp = 150
bonushp = 0

#defaultvars_attack
defaultattach = 0
attack = 0
bonusattack = 0

#enemyhp
enemyhp = 100


#inventory
consumables = []
helditems = []
xp = 0

#vars
attackrange = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

randomnos=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
spacer = ""

#consumables
consumabledict = {'potion':50,'berry':20,'water':10,'nothing':'nothing'}
battleconsumablesdict = {'poison':30}

#triggers
gridno = 9

#checks
maxpossiblehp = defaulthp+bonushp

