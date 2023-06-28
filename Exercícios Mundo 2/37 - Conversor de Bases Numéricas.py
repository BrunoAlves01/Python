print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opc = int(input('Para qual base deseja converter? '))
if opc == 1:
    dividendo = int(input('Digite o número: '))
    numero_digitado = dividendo
    quociente = 1
    lista = []
    while quociente >= 1:
        resto = dividendo % 2
        lista.insert(0, resto)
        quociente = dividendo // 2
        dividendo = quociente
        binario = ''.join([str(item) for item in lista])
        print(binario)
else:
    print('Selecione uma opção válida')