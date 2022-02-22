# IMC
peso = float(input('Peso em kg: '))
altura = float(input('Altura em cm: '))/100
imc = peso/(altura*altura)
if imc < 18.5:
    print(f'Seu IMC é de {imc}kg/m². Você está ABAIXO DO PESO. ({peso}kg e {altura}m)')
elif 18.5 <= imc < 25:
    print(f'IMC = {imc:.1f}kg/m². Você está com PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'IMC = {imc:.1f}kg/m². Você está no nível de SOBREPESO.')
elif 30 <= imc < 40:
    print(f'IMC = {imc:.1f}kg/m². Você está no nível de OBESIDADE.')
else:
    print(f'IMC = {imc:.1f}kg/m². Atenção, Você está no nível de OBESIDADE MÓRBIDA.')
