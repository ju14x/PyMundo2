# médias
p1 = float(input('Nota da P1: '))
p2 = float(input('Nota da P2: '))
media = float((p1 + p2) / 2)
if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
