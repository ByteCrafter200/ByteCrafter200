#Python program for random password generator

import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digit = '0123456789'
sym = '!@#$_^&*'

key = upper + lower + digit + sym

lenght = int(input("Enter the lenght of password: "))

word = random.sample(key,lenght)
password = "".join(word)

print("Your password is: ",password)

