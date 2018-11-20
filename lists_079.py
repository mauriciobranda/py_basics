
listx = list()

while True:

    va = int(input('Input a value: '))

    if listx.count(va) > 0:
        print('\n')
        print(f'O valor {va} ja existe, favor insira outro!')
        print('\n')
    else:
        listx.append(va)
        print(f'O valor {va} foi adicionado na lista!')
        print('\n')
        print(sorted(listx))
        print('\n')
    if va == 99:
        break
