import random
n1 = random.randrange(1, 5)
n2 = int(input('Estou pensando em um número de 1 à 5 , tente adivinhar:'))
if n2 == n1:
    print('Parabéns! Você acertou!')
else:
    print('Tente novamente!')