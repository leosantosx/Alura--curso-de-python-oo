from funcionario import Junior, Pleno

jose = Junior('José')
jose.buscar_perguntas_sem_respostas()

luan = Pleno('Luan')
luan.buscar_perguntas_sem_respostas()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)