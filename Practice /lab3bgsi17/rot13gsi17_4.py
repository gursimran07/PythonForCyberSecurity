#!/usr/bin/env python3

source_message = input("What is the message to encrypt/decrypt?")


shift = int(input("Enter the shift value: "))

source_message = source_message.lower()
final_message = ""

for letter in source_message:
    ascii_num = ord(letter)

    if 32 <= ascii_num <= 126:
        new_ascii = ascii_num + shift

        if new_ascii > 126:
            new_ascii = 32 + (new_ascii - 127)

        final_message += chr(new_ascii)
    else:
        final_message += chr(ascii_num)

print("Message has been converted:")
print(final_message)
