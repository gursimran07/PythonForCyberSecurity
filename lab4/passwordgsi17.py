#!/usr/bin/env python3



password = [
    "W4$acxyH7BtQiU3er",
    "Zk7i$F8uo#Aq",
    "L#1npOdATe2rjy",
    "vE@XsLwzKmy",
    "cBa6Hg7@uY3WjR",
    "QpiTcS7Ozlk2"
]

def check_password(password):
    errors = []
    if not any(char.islower() for char in password):
        errors.append("missing a letter between a-z")
    if not any(char.isupper() for char in password):
        errors.append("missing a letter between A-Z")
    if not any(char.isdigit() for char in password):
        errors.append("missing a number between 0-9")
    if not any(char in "$#@" for char in password):
        errors.append("missing a character from $#@")
    if len(password) > 16:
        errors.append("exceeds the maximum length allowed")
    if len(password) < 6:
        errors.append("minimum 6 characters required")
    if errors:
        return f"Incorrect because {','.join(errors)}"
    return "correct"

results = []
for pwd in password:
    result = f"{pwd}: {check_password(pwd)}"
    results.append(result)
    print(result)