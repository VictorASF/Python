print("-"*10 + "Pitando" + "-"*10)
a = float(input("Insira a altura da parede: "))
l = float(input("Insira a largura da parede: "))
print("Altura: {:.2f} - Largura: {:.2f} - Area: {:.2f}".format(a, l, a*l))
print("Sera preciso {:.2f} Litros de tinta".format((a*l)/3))