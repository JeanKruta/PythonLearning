import math
num1 = int(input("Digite a primeira coordenada em x: "))
num2 = int(input("Digite a primeira coordenada em y: "))
num3 = int(input("Digite a segunda coordenada em x: "))
num4 = int(input("Digite a segunda coordenada em y: "))

d = math.sqrt(((num1 - num2)**2) + ((num3 - num4)**2))

if d >= 10:
    print("longe")
else:
    print("perto")

input()