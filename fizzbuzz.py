num = int(input("Digite um número inteiro: "))

num2 = num % 3
num3 = num % 5

if num2 == 0 and num3 == 0:
    print("FizzBuzz")
else:
    print("", num)

input()