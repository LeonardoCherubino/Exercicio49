## Exercício 04-09: Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 

ValorCasa = float(input('Entre com o valor da casa. '))
Salário = float(input('Qual é o seu salário? '))
Anos = int(input('Quantos anos pra pagar? '))
Meses = Anos * 12
Prestação = ValorCasa / Meses
if Prestação > Salário * (30 / 100):
    print('Salário insuficiente. ')
else:
    print('Crédito aprovado. ')
    print('A prestação será de {}, durante {} meses. '.format(Prestação, Meses))
    print('Parabéns! ')
