import time

va_imovel = float(input('Valor do Imovel? '))
va_salario = float(input('Income? '))
va_anos = int(input('How long in years ? '))

def prestMensal(vi, anos):
    va_month = anos*12
    va_prest = vi/va_month
    return va_prest

trintaPerc = va_salario*(30/100)
valorSalMes = prestMensal(va_imovel, va_anos)

print("Valor da Prestacao: ")
print(prestMensal(va_imovel,va_anos))

print("30% do Salario: ")
print(trintaPerc)

if valorSalMes <= trintaPerc:
    print ("Calculando ...")
    time.sleep (5)
    print ("Crédito Aprovado, parabéns!")
else:
    print ("Calculando ...")
    time.sleep (5)
    print ("Crédito Negado, fale com seu gerente!")
