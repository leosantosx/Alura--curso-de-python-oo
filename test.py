from model import Filme, Serie

vingadores = Filme('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

lista = [vingadores, atlanta]
for programa in lista:
    print(programa)
