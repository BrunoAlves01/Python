km = int(input('Digite a velocidade:'))
if km >= 80:
    print('Você foi multado!')
    mul = (km - 80) * 7
    print('Valor da multa: R${},00'.format(mul))