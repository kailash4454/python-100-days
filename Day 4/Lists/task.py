# List in Python
fruits = ["cherry", "banana", "mango", "grapes", "orange"]
print(fruits)

# Accessing the members of list
print(fruits[0])
print(fruits[-1])
print(fruits[-5])

# Modifying items in a list
fruits[0] = "Apple"
print(fruits)

# Adding items at the end of list
fruits.append("lemon")
print(fruits)

# Adding a bunch of items together
fruits.extend(["pear", "cherry", "pineapple"])
print(fruits)


# insert an item
fruits.insert(1, "carrot")
print(fruits)

# Remove items
fruits.remove("pear")
print(fruits)
remove_item = fruits.pop(2)
print(remove_item)
print(fruits)

# clear whole list
games = ["cricket", "hokey"]
print(games)
games.clear()
print(games)

# gives index number of the specific item
print(fruits.index("mango"))

# counting the number of time an item is occurred in a list
fruits.append("orange")
count = fruits.count("orange")
print(count)

# sort the items of list
fruits.sort()
print(fruits)

# Reverse the order of items in a list
fruits.reverse()
print(fruits)

# copy a list
copy_list = fruits.copy()
print(copy_list)
print("\n")


# List Comprehension
squares1 = []
for x in range(5):
    squares1.append(x**2)

print(squares1)

squares2 = list(map(lambda x1: x1 ** 2, range(10)))
print(squares2)

squares3 = [x ** 2 for x in range(15)]
print(squares3)



