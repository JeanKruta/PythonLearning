numero_da_sorte = 7
numero_escolhido = int(input("Escolha um número de 1 a 30: "))

while numero_da_sorte != numero_escolhido:
    print("Você errou! Digite outro número novamente:")
    
    numero_escolhido = int(input("Escolha um número de 1 a 30: "))

print("Parabéns, você acertou o número!")