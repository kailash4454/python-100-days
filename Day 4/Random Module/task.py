import random
# from random import randint    //another way for importing module function
# import my_module

# Random integer generator
# rand_num = random.randint(1, 10)
# print(rand_num)
# print(my_module.my_fav_num)
# print("\n")

# Random Floating point generator
# rand_num_from_0_to_1 = random.random()
# print(rand_num_from_0_to_1)
# rand_float = random.random() * 10
# print(rand_float)
#
# rand_float_num = random.uniform(1, 10)
# print(rand_float_num)


# Coin Flip Program
random_num = random.randint(0, 1)
# print(random_num)
if random_num == 0:
    print("Heads")
else:
    print("Tails")
