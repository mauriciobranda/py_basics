import datetime

count = 0

def maiorDezoito(x):
    year_now = 2018
    dif_ano = year_now - x
    if dif_ano >= 18 :
        return 1
    else:
        return 0

for c in range(0,7):
    ano = int (input ('Passo: '))
    if maiorDezoito(ano) == 1: #Maior de Dezoito
        count = count + 1

print ("O numero de maiores de dezoito anos é de: "+str(count))
