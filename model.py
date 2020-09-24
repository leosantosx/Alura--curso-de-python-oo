class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{super().__str__()} - Duração: {self.duracao}'

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{super().__str__()} - Temporadas: {self.temporadas}'

if __name__ == '__main__':
    vingadores = Filme('vingadores', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)

    lista = [vingadores, atlanta]
    for programa in lista:
        print(programa)

