from time import sleep

a = float(input('Insira a medida do primeiro lado do triângulo: '))
b = float(input('Insira a medida do segundo lado do triângulo: '))
c = float(input('Insira a medida do terceiro lado do triângulo: '))
print('Aguarde ...')
sleep(2)
print('\n\n')
if (a < (b+c) and b < (a+c) and c < (a+b)):
    print('Estas medidas satisfazem a condição de existência de um triângulo.')
else:
    print("Estas medidas não podem formar um triângulo.")﻿