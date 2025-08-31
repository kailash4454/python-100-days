import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(len(friends))

# 1st option
rand_index = random.randint(0, 4)
print(friends[rand_index])

# 2nd option
print(random.choice(friends))
