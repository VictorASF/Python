np = float(input('Peso: '))
na = float(input('Altura: '))
imc = np/(na**2)

print('IMC: {:.2f}'.format(imc))
if imc<18.5:
    print('Abaixo do peso ideal')
elif 18.5<imc<25:
    print('Peso ideal')
elif 25<imc<30:
    print('Sobrepeso')
elif 30<imc<40:
    print('Obesidade')
else:
    print('Obesidade morbida')