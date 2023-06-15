from random import choice
pri = input('Primeiro Aluno: ')
seg = input('Segundo Aluno: ')
ter = input('Terceiro Aluno: ')
qua = input('Quarto Aluno: ')
lista = [pri, seg, ter, qua]
esc = choice(lista)
print('O Aluno escolhido foi {}'.format(esc))