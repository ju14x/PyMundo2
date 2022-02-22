# serviço militar
ano = int(input('Insira seu ano de nascimento: '))
idade = 2022 - ano
if idade < 18:
    print('Você ainda não tem 18 anos, mas fique atento para o momento de se alistar!'
          '\nFaltam {} anos para o seu alistamento militar.'.format(18 - idade))
elif idade == 18:
    print('Você tem 18 anos, portanto, a hora de se alistar é agora!')
else:
    print('Você já passou dos 18 anos e está {} anos após o prazo de alistamento militar.'.format(idade - 18))
