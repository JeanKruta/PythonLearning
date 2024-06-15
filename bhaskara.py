import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) -4 * (a) * (c)

if delta >= 0:
  S1 = (-b + math.sqrt(delta)) / (2 * a)
  S2 = (-b - math.sqrt(delta)) / (2 * a)
  if S1 != S2:
    print("As raízes da equação são: ", sorted([S1, S2]))
  else:
    print("A raíz dupla desta equação é: ", S1)

else:
  print("esta equação não possui raízes reais.")

input()
