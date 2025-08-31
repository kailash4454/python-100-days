import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
# if user_input == 0:
#     print(rock)
# elif user_input == 1:
#     print(paper)
# elif user_input == 2:
#     print(scissors)
# else:
#     print("You have chosen the wrong value")
#     exit()

game_images = [rock, paper, scissors]

if user_input >= 0 and user_input <= 2:
    print(game_images[user_input])
else:
    print("You have chosen the wrong value. You lose")
    exit()

print("Computer Chose: ")
rand_num = random.randint(0, 2)
# if rand_num == 0:
#     print(rock)
# elif rand_num == 1:
#     print(paper)
# else:
#     print(scissors)

print(game_images[rand_num])

if user_input == rand_num:
    print("it's a Draw")
elif user_input == 2 and rand_num == 0:
    print("You Lose")
elif user_input == 0 and rand_num == 2:
    print("You Win!")
elif user_input > rand_num:
    print("You Win!")
else:
    print("You Lose")