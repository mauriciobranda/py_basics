import time
formaGelo = 'vazia'
tempo = 0

while formaGelo == 'vazia':
    pergunta = input('A forma de gelo ainda esta vazia ? [S][N] ')

    if pergunta == 'S':
        print('Entao deixe a torneira aberta para que preencha.')
        #sleep(2)
    else:
        print('Beleza, entao agora pode levar ao freezer !')
        break

