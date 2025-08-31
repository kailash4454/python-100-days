print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# print('''
#           ___   ____
#         /' --;^/ ,-_\     \ | /    | | | /| | "|" | |\| /"_  "|" /"\  |_) |_"
#        / / --o\ o-\ \\   --(_)--   |/|/ /"| |  |  | | | \_|   |  \_/  |_&gt; |__
#       /-/-/|o|-|\-\\|\\   / | \
#        '`  ` |-|   `` '               |") |_" (_" /"' | | |_" |"\
#              |-|                      |"\ |__ ,_) \_, |_| |__ |_/  o  o  o
#              |-|O
#              |-(\,__
#           ...|-|\--,\_....
#       ,;;;;;;;;;;;;;;;;;;;;;;;;,.
# ~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? \n      "
      " Type 'left' or 'right'")

direction = input()

if direction.lower() == "left":
    # print('You\'ve come to a lake. There is an island in the middle of the lake. \n '
    #       'Type "wait" to wait for a boat.'
    #       ' Type "swim" to swim across.')

    choose_way = input('You\'ve come to a lake. There is an island in the middle of the lake. \n '
                       'Type "wait" to wait for a boat.'
                       ' Type "swim" to swim across.\n')

    if choose_way.lower() == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors. \n"
              " One red, one yellow and one blue. "
              "Which colour do you choose?")

        choose_door = input().lower()
        if choose_door == "red":
            print(" Burned by fire.\n    Game Over.")
        elif choose_door == "blue":
            print(" Eaten by beasts.\n   Game Over.")
        elif choose_door == "yellow":
            print(" You found the tressure.\n    You Win!")
        else:
            print(" Game Over.")

    else:
        print(" Attacked by trout.\n     Game Over.")

else:
    print(" Fall into a hole.\n  Game Over.")