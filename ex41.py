# categoria do atleta
print('--CONFEDERAÇÃO NACIONAL DE NATAÇÃO--')
ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')
