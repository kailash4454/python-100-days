alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.


# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.



# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# first attempt, so many code repetition and complex

# def caesar(original_text, shift_amount):
#     if direction == "encode":
#         def encrypt(original_text, shift_amount):
#             cipher_text = ""
#             for letter in original_text:
#                 shifted_position = alphabet.index(letter) + shift_amount
#                 shifted_position %= len(alphabet)
#                 cipher_text += alphabet[shifted_position]
#             print(f"Here is the encoded result: {cipher_text}")
#
#         encrypt(original_text=text, shift_amount=shift)
#     elif direction == "decode":
#         def decrypt(original_text, shift_amount):
#             cipher_text = ""
#             for letter in original_text:
#                 shifted_position = alphabet.index(letter) - shift_amount
#                 shifted_position %= len(alphabet)
#                 cipher_text += alphabet[shifted_position]
#             print(f"Here is the decoded result: {cipher_text}")
#
#         decrypt(original_text=text, shift_amount=shift)
#     else:
#         print("You typed wrong word.")

# second attempt, some point of simplification

# def caesar(original_text, shift_amount, dir):
#     cipher_text = ""
#     if dir == "encode":
#         for letter in original_text:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             cipher_text += alphabet[shifted_position]
#     elif dir == "decode":
#         for letter in original_text:
#             shifted_position = alphabet.index(letter) - shift_amount
#             shifted_position %= len(alphabet)
#             cipher_text += alphabet[shifted_position]
#     else:
#         print("You typed wrong word.")
#         exit()
#
#     print(f"Here is the {dir} result: {cipher_text}")


#Third attempt more simplified and no code redundancy.

def caesar(original_text, shift_amount, dire):
    if dire == "encode":
        mult = 1
    elif dire == "decode":
        mult = -1
    else:
        print("You typed wrong word.")
        exit()

    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount * mult
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the {dire}d result: {cipher_text}")

caesar(text, shift, direction)