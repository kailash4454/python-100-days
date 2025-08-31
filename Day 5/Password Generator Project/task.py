import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Easy version
# # let_str = ""
# # num_str = ""
# # sym_str = ""
# easy_pwd = ""
# for let in range(nr_letters):
#     # let_str += random.choice(letters)
#     # print(let_str)
#     easy_pwd += random.choice(letters)
#
# for sym in range(nr_symbols):
#     easy_pwd += random.choice(symbols)
#
# for num in range(nr_numbers):
#     easy_pwd += random.choice(numbers)
#
# # easy_pwd = let_str + sym_str + num_str
# print(f"Your easy password is: {easy_pwd}")
#
#
# # Hard Version
# len_str = len(easy_pwd)
# # print(len_str)
#
# hard_pwd = ""
# str_char = list(easy_pwd)
# random.shuffle(str_char)
# hard_pwd = hard_pwd.join(str_char)
#
# print(f"Your hard password is: {hard_pwd}")

password_list = []
for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
# for char in range(len(password_list)):            # it's true also ,but it's a long way
#      password += password_list[char]

for char in password_list:
     password += char
print(f"Your Password is: {password}")
