#TypeError
# These errors occur when you are using the wrong data type. e.g. len(12345)
len("12345")  # len(12345)

# Type Checking
print(type("hello"))
print(type(123))
print(type(3.14))
print(type(True))
print("\n")

# Type Conversion
print("123" + "456")
print(int("123") + int("456"))
# print(int("abc"))   ValueError: invalid literal for int() with base 10: 'abc'

print("Number of letters in your name: " + str(len(input("Enter your name"))))