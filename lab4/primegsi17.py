#!/usr/bin/env python3
def prime(n):
    if n  <=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(1, 101):
    print(f"{number}: {'Prime' if prime(number) else 'Not a Prime number'}")    