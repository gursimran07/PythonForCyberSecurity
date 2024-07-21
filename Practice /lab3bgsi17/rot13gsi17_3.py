#!/usr/bin/env python3

source_message = input("What is the message to encrypt/decrypt?")

shifted_message = ""
final_message = ""

for letter in source_message:
    ascii_num = ord(letter)
    
    
    new_ascii = ascii_num + 26

    if new_ascii > 126:
        new_ascii = 32 + (new_ascii - 127)

   
    shifted_char = chr(new_ascii)
    shifted_message += shifted_char

    if shifted_char.islower():
        shifted_char = shifted_char.upper()
    elif shifted_char.isupper():
        shifted_char = shifted_char.lower()

    final_message += shifted_char

print("Shifted message:")
print(shifted_message)
print("Message has been converted:")
print(final_message)
