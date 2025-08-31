print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S" or size == "s":
    #print("price of Small pizza(S) is $15")
    bill = 15

elif size.lower() == "m":
    #print("price of Medium pizza(S) is $20")
    bill = 20

elif size.lower() == "l":
    #print("price of Large pizza(S) is $25")
    bill = 25
else:
    print("Unrecognized size. please enter the correct size")
    exit()

if pepperoni.lower() == "y":
     if size.lower() == "s":
        bill += 2
     else:
         bill += 3

if extra_cheese.lower() == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")