import numpy as np

matriz_1 = np.array([[1, 2, 3,4], [10, 20, 30, 40,], [100, 200, 300, 400]])
matriz_2 = np.array([[3, 4, 5, 6], [11, 34, 23, 11], [300, 123, 11, 1]])
print(matriz_1)
print(matriz_2)

soma_das_matrizes= matriz_1 + matriz_2
print(soma_das_matrizes)

multiplicacao_das_matrizes = matriz_1 * matriz_2
print(multiplicacao_das_matrizes)

#vale para subtração / divisão de matrizes não existe

## Multiplicação de matrizes usando o .dot (a primeira matriz precisa ter o número de linhas igual o número de colunas da segunda)
#Para isso podemos usar o .T para fazer uma transposição(Transpose)
#(Matriz_1 + Matriz_2).T = (Matriz_1.T) + (Matriz_2.T)

matriz2_transposta = matriz_2.T
multiplicacao_das_matrizes2 = np.dot(matriz_1, matriz2_transposta )

print(multiplicacao_das_matrizes2)


#########################################################################################

#Matriz Inversa é uma matriz obtida através de uma matriz quadrada (número de linhas igual o de colunas)

##Uma matriz A deve ser multiplicada por uma matriz A**-1(a matriz A Inversa) para obtermos a Matriz Identidade
### O determinante da Matriz A precisa ser != de 0

Matriz_A = np.array([[15, 23, 25, 44], [12, 33, 45, 67], [11, 10, 1, 3], [2, 5, 6, 7]])

determinante_matriz_A = np.linalg.det(Matriz_A)
print(determinante_matriz_A) # Resultado diferente de 0 --> Então a Matriz A tem matriz inversa

matriz_A_inversa = np.linalg.inv(Matriz_A)
print(matriz_A_inversa)

matriz_identidade = np.dot(Matriz_A, matriz_A_inversa) #.dot --> Faz o produto escalar
print(matriz_identidade) #Todos os elementos da diagonal principal esquerda - direita / cima - baixo = 1 / o restante deveria ser = 0


#Determinante da Matriz

##Gerar matriz aleatória 
matriz_random_1 = np.random.randint(0, 30, size = (3,3))
print("Matriz aleatrória 1: ", matriz_random_1)
