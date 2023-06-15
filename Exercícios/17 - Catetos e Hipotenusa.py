from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Commprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))