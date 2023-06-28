km = int(input('Digite a distancia da viagem: '))
if km >= 199:
    n = km * 0.50
else:
    n = km * 0.45
print('A sua viagem vai custar R${:.2f}'.format(n))