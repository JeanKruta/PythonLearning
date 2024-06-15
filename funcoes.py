#função inicial

def saudação():
    print("Seja bem vindo(a)! É um prazer recebê-lo(a)")
    print("Faça o cadastro abaixo!")

saudação()

#função com parâmetros

def saudação(nome):
    print(f"Seja bem vindo(a), {nome}! É um prazer recebê-lo(a)")
    print("Faça o cadastro abaixo!")

saudação("Jean")

#função com parâmetros default

def saudação(nome = "Roberta"):
    print(f"Seja bem vindo(a), {nome}! É um prazer recebê-lo(a)")
    print("Faça o cadastro abaixo!")

saudação()

#Função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(10, 30)

print("A soma é: ", resultado)