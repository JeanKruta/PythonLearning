#criar dicionário
dicionario = {} #vazio
dicionario = dict() #vazio

dicionario = {"nome" : "Jean", "idade" : 27, "altura" : 1.73}
print(dicionario)

print(dicionario["idade"])

#adicionar elementos / se ja existir o conteúdo adicionado, irá substituir

dicionario["Programador"] = True
print(dicionario)

#Iterando sobre um dicionário

for variavel in dicionario:
    print(variavel, dicionario[variavel])

#Testar existência de uma chave

print("peso" in dicionario)
print("altura" in dicionario)