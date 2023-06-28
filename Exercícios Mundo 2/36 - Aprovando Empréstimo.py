val = float(input('Qual o valor da casa? '))
ano = int(input('Em quantos anos você irá pagar? '))
sal = float(input('Qual é o seu salário? '))
ano2 = ano * 12
pres = val / ano2
res = (sal / 10) * 3
print('Será em {} meses'.format(ano2))
print('Será R${:.2f} por mês'.format(pres))
if pres<res:
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado')