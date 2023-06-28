sal = int(input('Digite seu salário: '))
if sal <= 1250:
    sal2 = (sal / 15) + sal
    print('Seu novo salário vai ser de R${:.2f}'.format(sal2))
else:
    sal3 = (sal / 10) + sal
    print('Seu novo salário será de R${:.2f}'.format(sal3))