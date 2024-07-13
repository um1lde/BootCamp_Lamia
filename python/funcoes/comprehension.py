from functools import reduce

alunos = [ 
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael ', 'nota': 6.7},
]

somar = lambda a,b: a+ b

aluno_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
print(aluno_aprovados)

notas_alunos_aprovados = [aluno['nota'] for aluno in aluno_aprovados]
print(notas_alunos_aprovados)

total = reduce(somar, notas_alunos_aprovados, 0)
print(total / len(aluno_aprovados))



