# Empréstimo
print('(-------------------------)\n'
      'Para analisarmos seu pedido de empréstimo, nos informe os seguintes dados: '
      '\n(-------------------------)')
valor_casa = int(input('O valor da casa é de (R$): '))
salario = int(input('Seu salário é de (R$): '))
anos = int(input('Em quantos anos pretende pagar? '))

prest = (valor_casa / (anos * 12))
print('(-------------------------)\n'
      'Para o cenário calculado, a prestação mensal será de R${:.2f}, a ser paga durante {} anos (ou {} meses).'
      '\n(30% do salário: R${})'.format(prest, anos, anos*12, int(0.3*salario)))
if prest > (int(0.3*salario)):
    print('Dadas as condições, infelizmente o financiamento foi negado. Para ser aprovado, a prestação '
          'precisa ser menor ou  igual a 30% (R${}) do seu salário.'.format(int(0.3*salario)))
else:
    print('Empréstimo aprovado!')
