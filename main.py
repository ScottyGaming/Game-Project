#import codes
from random import *
from time import sleep
from func_stats import *
from func_menu import *

#Grid
#starting game
print('   |\                     /)')
print('  /\_\\__               (_//')
print(' |   `>\-`     _._      //`)')
print('  \ /` \\  _.-`:::`-._  //')
print('   `    \|`    :::    |/')
print('         |     :::     |')
print('         |.....:::.....|')
print('         |:::::::::::::|')
print('         |     :::     |')
print('         \     :::     /')
print('          \    :::    /')
print('           `-. ::: .-')
print("            //`:::`\\")
print("           //   '   \\")
print('          |/         \\')
print()
input(" -- Weird Dungeon Explore Game I Made --\n\nPress any button except the power off button to start!\n")
print(spacer)

def start():
  start = int(input("Enter starting grid number (3x3): "))
  if start>9 or start<1:
    print("Out of bounds! Enter slot 1-9!")
    print("Relaunch Program XD")
    input("Press any key to exit")
    quit()
  else:
    print(grid_pos[start])
    
start()
#Game Loop
while True:
    print()
    menu()
    

    


