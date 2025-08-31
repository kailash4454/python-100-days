for num in range(1, 10):    # will be not included in this
    print(num)
print("\n")

for num in range(1, 11, 2):   # same here 11 where not included. it will go from 1 to 10 only.
    print(num)


# Calculating the sum of numbers from 1 to 100
total = 0
for num in range(1, 101):
    total += num

print(total)