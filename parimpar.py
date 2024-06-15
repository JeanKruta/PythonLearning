num = int(input("Digite um número: "))

if num != 0:
  num2 = num % 2
  if num2 == 0:
      print("Este é um número par.")
  else:
      print("Este é um número ímpar.")
else:
  print("Este é um número neutro!")

input("Aperte <enter> para fechar o programa.")