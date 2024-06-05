import random
import string

length=int(input("Enter length:"))

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)

chars =string.ascii_letters
chars +=string.digits
chars +=string.punctuation


password =""

for i in range(length):
    password +=random.choice(chars)


print("Your random password:",password)

