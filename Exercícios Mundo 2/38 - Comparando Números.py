n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 == n2:
    print('Não existe valor maior, os dois são iguais')
elif n1 > n2:
    print('O valor {} que é o primeiro é maior'.format(n1))
else:
    print('O valor {} que é o segundo valor é menor'.format(n2))
