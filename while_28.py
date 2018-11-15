from random import *

contaTentativas = 10
numRandom = randint(0,9)
valor = 0

while int(numRandom) != int(valor):
    valor = input ("Diz aí um numero de 0 a 10 !? ")
    #print("Valor do PC: "+str(numRandom))
    #print ("Valor do Gamer: " + str (valor))
    contaTentativas = contaTentativas + 100

if int(numRandom) == int(valor):
    print("Acertou ! O numero que pensei foi "+str(numRandom)+"!")

print("Voce fez "+str(contaTentativas)+ " tentativas!")
