tama = '''
     ___-----------___
   --                 --
  /                     \\
 /   |---------------|   \\
|    |               |    |
|    |     ({})     |    |
|    |               |    |
|    |---------------|    |
 \                       /
  \    |  O  O  O  |    /
    --_______________--
'''

import random

name = input("What is your Tamagotchi's name? ")

hunger = 50
happiness = 50
health = 100
behavior = 100
age = 0

'''
CONDITION
The game continues as long as...
'''
while
    print("Your commands: ")
    print("- eat")
    print("- clean")
    print("- play")
    print("- doctor")
    print("- discipline")
    
    answer = input("What do you want to do?    ").lower()
    if answer == "eat":
        '''
        EATING
        if hunger > 50, they will lose 20 health
        if hunger < 50, their hunger is set back to 100
        '''
    elif answer == "clean":
        '''
        CLEANING
        50% chance to decrease happiness by 30 and behavior by 25
        '''
    elif answer == "play":
        '''
        PLAYING
        decreases hunger by 20
        increases happiness by 30
        '''
    elif answer == "doctor":
        '''
        DOCTORING
        25% chance to decrease behavior by 50
        increases health by 30
        '''
    elif answer == "discipline":
        '''
        DISCIPLINING
        if behavior > 50, happiness decreases by 25
        otherwise, 50% chance to set behavior back to 100
        '''

    '''
    LIVING
    hunger goes down by 10 each turn
    if hunger < 0, they lose 15 health and 15 happiness
    if happiness < 0, they lose 15 health each turn
    increase age by 1 each turn
    '''

    if health > 75:
        print(tama.format("-U-"))
    elif health > 50:
        print(tama.format("o_o"))
    elif health > 25:
        print(tama.format(">_<"))
    else:
        print(tama.format("/_\\"))

    print()

print("Oh no!", name, "died!")
print(name, "survived", age, "days.")
print(tama.format("X_X"))
