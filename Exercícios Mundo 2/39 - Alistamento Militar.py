from datetime import date
ano = date.today().year
idade = int(input('Informe o ano de nascimento: '))
conta = ano - idade
if conta >= 18 and <= 45:
    print('Você ainda irá se alistar para o serviço militar')
##elif conta >= 18:
    ##print('Está na hora de se alistar no serviço militar ')
elif conta >=45:
    print('Você já passou da hora')