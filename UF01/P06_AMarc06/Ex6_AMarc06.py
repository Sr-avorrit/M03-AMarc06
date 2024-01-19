num = int(input('Enter a number: '))
for i in range(num + 1):
    for j in range(num - i + 1):
        print(f' {i}/{j} |', end='')
    print('')