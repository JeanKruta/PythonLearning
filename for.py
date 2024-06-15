#for variavel in range(10):
    #print(variavel)


#for variavel in range(1, 11):
    #print(variavel)

#for variavel in range(1, 100, 3):
    #print(variavel)

#Exemplo prático

soma = 0

for i in range(1, 5):
    nota = float(input(f"Informe a nota {i}: ")) #o f depois do input significa que é um fstring, com isso conseguimos injetar uma variável dentro da string (variável {i})
    soma = soma + nota
    media = soma / 4
print("A média das notas é: ", media)