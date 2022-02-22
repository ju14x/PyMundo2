# comparação de números inteiros
a = int(input('Valor A: '))
b = int(input('Valor B: '))
if a > b:
    print(f'A ({a}) é maior que B ({b})')
elif b > a:
    print(f'B ({b}) é maior que A ({a})')
else:
    print(f'Os valores inseridos são iguais. ({a})')
