
nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if (nota >= 9 and comportado):
    print('\nDuas palavras para bens! :P')
    print('Quadro de Honra ')
elif (nota >=7):
    print('Aprovado')
elif (nota >= 5.5):
    print('Recuperação')
elif (nota >= 4):
    print('Recuperação + Trabalho')
elif (nota >= 3.5):
    print('Recuperação + Trabalho')
else:
    print('Reprovado')
# iremos entrar no conceito de bloco

print(nota)
