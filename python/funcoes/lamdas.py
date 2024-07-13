from functools import reduce

alunos = [ 
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael ', 'nota': 6.7},
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7

# from map_reduce import somar
somar = lambda a,b: a+ b

# aluno_honra = lambda aluno: aluno['nota'] >= 9

obter_nota = lambda aluno: aluno['nota']

                            #  função e depois a lista
aluno_aprovados = list(filter(aluno_aprovado, alunos)) #vai filtrar em aluno aprovados os nomes dos alunos aprovados com media acima ou igual a 7
notas_alunos_aprovados = list(map(obter_nota,aluno_aprovados))

# print(notas_alunos_aprovados)

# print(obter_nota(alunos[2]))

# print(aluno_aprovados) 

total = reduce(somar, notas_alunos_aprovados, 0)
print(total / len(aluno_aprovados))

#funcao lambda, com paramentro aluno, funcao de unica linha
# print(alunos)

