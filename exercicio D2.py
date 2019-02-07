from math import cos, sin, tan, radians

ang = float(input("Insira um angulo: "))
rad = radians(ang)
print("Angulo: {} - Cosseno: {:.2f} - Seno: {:.2f} - Tangente: {:.2f}".format(ang, cos(rad), sin(rad), tan(rad)))