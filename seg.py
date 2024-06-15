segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))


dias = segundos / 86400
segundos_restantes = segundos % 86400

horas = segundos_restantes / 3600
segundos_restantes %= 3600

minutos = segundos_restantes / 60
segundos_rest = segundos_restantes % 60

dias = int(dias)
horas = int(horas)
minutos = int(minutos)
segundos_rest = int(segundos_rest)


print(dias, "dias", horas, "horas", minutos, "minutos", segundos_rest, "segundos")

input("Digite <enter> para fechar o programa.")