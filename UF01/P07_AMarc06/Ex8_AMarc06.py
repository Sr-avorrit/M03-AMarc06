msg = input("Enter a mesage to encript: ")
key = int(input("Enter the encription key: "))
emsg = ''
for i in msg:
    emsg += chr((ord(i) + key-65) % 26 + 65) if i.isupper() else chr((ord(i) + key-97) % 26 + 97)
print(emsg)