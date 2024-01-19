passw = input("Enter a password: ")
maju = len(''.join(i for i in passw if i.isupper()))
minu = len(''.join(i for i in passw if i.islower()))
nums = len(''.join(i for i in passw if i.isnumeric()))

if maju > 0 and minu > 0 and nums > 0 and maju+minu+nums < len(passw) and len(passw) >= 8:
    print("The password is correct!")
else:
    print("The password does not has the minimun requisites!")