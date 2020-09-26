class Funcionario:

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mes')

class Alura(Funcionario):
    def __init__(self, nome):
        self.nome = nome

    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def buscar_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Senior(Alura, Caelum):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass






