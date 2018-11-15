idade = 0
idade_old = 0
idade_media = 0
h_old = ''
count_young = 0

for c in range(0,2):
    nome = input("Digite um nome: ")
    sexo = input ("Digite o sexo [M][F]: ").upper()
    idade = int(input ("Digite a idade: "))
    idade_media = idade_media + idade

    if sexo == "F" and idade < 20:
        count_young = count_young + 1

    if sexo =="M" and idade > idade_old:
        idade_old = idade
        h_old = nome

print("A idade média do grupo é "+str(idade_media/2)+ " anos")
print("Existem "+str(count_young)+" mulheres menores de 20 anos")
print("O home mais velho chama-se "+h_old)



