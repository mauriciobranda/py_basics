listx = list()
tamanhoDaLista = 0

for cpos in range(0,5):
    cval = int(input('Input a value: '))
    #tamanhoDaLista = listx.count(cpos)

    if cpos == 0:
        listx.append(cval)
        print('Adicionado no final da Lista! ')
    elif cval > listx[-1]:# maior que o ultimo elemento ?
        listx.append(cval)
    else:
        pos = 0
        while pos < len(listx):
            if cval <= listx[pos]:
                listx.insert(pos, cval)
                print(f'Valores added na pos: {pos}')
                break
            pos += 1
print('-='*30)
print(f'Valores em ordem: {listx}')



