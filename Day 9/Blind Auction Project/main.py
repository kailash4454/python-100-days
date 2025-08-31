from art import logo
# from os import system
print(logo)
print("Welcome to the Secret Auction Program.")

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


# First attempt by me

# bid_dictionary = {}
#
# restart = "yes"
# while restart == "yes":
#     name = input("What is your name?: ")
#     bid_value = int(input("What is your bid?: $"))
#     bid_dictionary[name] = bid_value
#     restart = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#     print("\n" * 100)
#     # system("cls")
#
# res = max(bid_dictionary, key=bid_dictionary.get)
# print(f"The Winner is {res} with a bid of ${bid_dictionary[res]}.")


# Second Attempt

def highest_bidder_calculate(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder

    print(f"The Winner is {winner} with a bid of ${highest_bid}.")

bid_dictionary = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid_value = int(input("What is your bid?: $"))
    bid_dictionary[name] = bid_value
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if restart == "no":
        continue_bidding = False
        highest_bidder_calculate(bid_dictionary)
    elif restart == "yes":
        print("\n" * 100)

