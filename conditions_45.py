import time
import string, random

while va_escolha_player
va_escolha_player = input('(a)Pedra, (b)Tesoura ou (c)Papel? ')

foo = ['a', 'b', 'c']
va_escolha_cpu = random.choice(foo)

def f(x):
    return {
        'a': 1,
        'b': 2,
        'c': 3
    }.get(x, 0)

if f(va_escolha_player) == 1 and f(va_escolha_cpu) == 2:
    print ('Você escolheu PEDRA !')
    print ('CPU escolheu TESOURA !')
    print('Você venceu !')
elif f(va_escolha_player) == 1 and f(va_escolha_cpu) == 3:
    print ('Você escolheu PEDRA !')
    print ('CPU escolheu PAPEL !')
    print ('Você perdeu !')
elif f(va_escolha_player) == 2 and f(va_escolha_cpu) == 1:
    print ('Você escolheu TESOURA !')
    print ('CPU escolheu PEDRA !')
    print ('Você perdeu !')
elif f(va_escolha_player) == 2 and f(va_escolha_cpu) == 3:
    print ('Você escolheu TESOURA !')
    print ('CPU escolheu PAPEL !')
    print ('Você venceu !')
elif f(va_escolha_player) == 3 and f(va_escolha_cpu) == 1:
    print ('Você escolheu PAPEL !')
    print ('CPU escolheu PEDRA !')
    print ('Você venceu !')
elif f(va_escolha_player) == 3 and f(va_escolha_cpu) == 2:
    print ('Você escolheu PAPEL !')
    print ('CPU escolheu TESOURA !')
    print ('Você perdeu !')
elif f(va_escolha_player) == f(va_escolha_cpu) :
    print ('Você escolheu o mesmo que o CPU !')
    print ('Empate !')
else:
    print ('Opção invalida !')
