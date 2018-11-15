#59


valor1 = input ("Valor 1: ")
valor2 = input ("Valor 2: ")

choice ='0'
while choice =='0':
    print("[1]Do the Sum")
    print("[2]Do a Multiply")
    print("[3]Find the Greater value")
    print("[4]Pick new numbers")
    print("[5]Ciao/Good Bye")

    choice = input ("Please make a choice: ")

    if choice == "5":
        print("Good bye!")
        sys.exit ()
    elif choice == "4":
        print ("-------------------------------")
        print ("-------------------------------")
        valor1 = input ("Diga o novo valor 1: ")
        valor2 = input ("Diga o novo valor 2: ")
        choice = '0'
    elif choice == "3":
        if valor1 > valor2:
            print ("-------------------------------")
            print ("-------------------------------")
            print (valor1 + " é maior que "+ valor2)
            choice = '0'
        elif valor2 > valor1:
            print ("-------------------------------")
            print ("-------------------------------")
            print (valor2 + " é maior que "+ valor1)
            choice = '0'
        else:
            print ("-------------------------------")
            print ("-------------------------------")
            print (valor2 + " é igual ao valor " + valor1)
            choice = '0'
    elif choice == "2":
        multip = int(valor1) * int(valor2)
        print ("-------------------------------")
        print ("-------------------------------")
        print ("A multiplicacao dos valores é: " + str (multip))
        choice = '0'
    elif choice == "1":
        soma = int(valor1) + int(valor2)
        print ("-------------------------------")
        print ("-------------------------------")
        print("A soma dos valores é: "+str(soma))
        choice = '0'
    else:
        print("I don't understand your choice.")﻿