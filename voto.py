idade = input("Digite sua idade: ")
idade = int(idade)

if idade >= 18:
   print("Você deve votar!")

elif idade >= 65 or idade == 16 or idade == 17:
   print("Você pode votar caso queira.")

else:
   print("Você não pode votar!")

input("Pressione <enter> para fechar o programa.")