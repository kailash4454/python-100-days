print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("child ticket price is $5.")
        bill = 5
    elif age <= 18:
        print("youth ticket price is $7.")
        bill = 7
    else:
        print("adult ticket price is $12.")
        bill = 12

    want_photo = input("do you like to take photo? type y for yes or n for no.")
    if want_photo == "y":
        # add extra $3 to the bill
        bill += 3

    print(f"total bill to pay is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
