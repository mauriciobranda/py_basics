lista = list()

for c in range(0,5):
    va = int(input('Input a value: '))
    lista.append(va)

maiorValor = 0
menorValor = 0

for c in range(0,5):

    if c == 0:
        maiorValor = lista[c]
        maiorValorPos = c

    if lista[c] > maiorValor:
        maiorValor = lista[c]
        maiorValorPos = c

for c in range(0,5):

    if c == 0:
        menorValor = lista[c]
        menorValorPos = c

    if lista[c] < menorValor:
        menorValor = lista[c]
        menorValorPos = c

print(f'O maior valor eh {maiorValor} na posicao {maiorValorPos}!')
print(f'O menor valor eh {menorValor} na posicao {menorValorPos}!')