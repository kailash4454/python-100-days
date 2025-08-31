alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# first attempt code written by me which contain so many Repetition and made code so much complex to understand.

# def encrypt(original_text, shift_amount):
#     index_list = []
#     for char in original_text:
#         index_list.append(alphabet.index(char))
#     # print(index_list)
#
#     new_index_list = []
#     for index in index_list:
#         new_index = index + shift_amount
#         if new_index >= 25:
#             new_index -= 26
#
#         new_index_list.append(new_index)
#     # print(new_index_list)
#
#     encrypt_str = ""
#     for index in new_index_list:
#         encrypt_str += alphabet[index]
#
#     print(f"Here is the encoded result: {encrypt_str}")


# Second attempt made code simple and reduce repetition.

# def encrypt(original_text, shift_amount):
#     encrypt_str = ""
#     for char in original_text:
#         index_num = alphabet.index(char)
#         index_num += shift_amount
#         if index_num >= 25:
#             index_num %= 26
#
#         encrypt_str += alphabet[index_num]
#
#     print(f"Here is the encoded result: {encrypt_str}")


# Third attempt made it more simple and precise and eliminate the code redundancy.

def encrypt(original_text, shift_amount):
    encrypt_str = ""
    for char in original_text:
        index_num = alphabet.index(char) + shift_amount
        index_num %= len(alphabet)

        encrypt_str += alphabet[index_num]

    print(f"Here is the encoded result: {encrypt_str}")


encrypt(text, shift)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

