
vontade = input('Voce quer atravessar a rua ? [S][N]')

if vontade == 'S':
    print('Olhe para a direita')
    print('Olhe para a esquerda')

    carro = input('Tem carro vindo ? [S][N]')

    if carro == 'S':
        print('Espere')
    else:
        print('Pode atravessar entaoooo !')
        print('Voce atravessou a rua !!!!')

