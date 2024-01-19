import random
import string

maju = string.ascii_uppercase
minu = string.ascii_lowercase
nums = string.digits
simb = string.punctuation

passww = ''
passw = ''

for i in range(4):
    for j in range(random.randint(2, 4)):
        if i == 0:
            passww += maju[random.randrange(len(maju))]
        elif i == 1:
            passww += minu[random.randrange(len(minu))]
        elif i == 2:
            passww += nums[random.randrange(len(nums))]
        else:
            passww += simb[random.randrange(len(simb))]

while len(passww) > 0:
    leter = passww[random.randrange(len(passww))]
    passw += leter
    passww = passww[:passww.index(leter)]+''+passww[passww.index(leter)+1:]

print(passw) 