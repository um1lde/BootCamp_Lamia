a = 'valor'
# true 
a = 0 
# false
a= -1 # qualquer numero diferente de 0 sera avaliado como verdadeiro
# true
a = '' # string vazia vai para falso
# false
a = ' ' # com espaco em branco sera avaliada como verdadeira
# True
a = [] # lista vazia falsa
# false
a = {} # conjunto vazio falso
# false

print(not 'valor')
# vai avaliar para falso

print(not not 'valor') 
# vai avaliar para verdadeiro

if a:
    print('Existe!!!!')
else:
    print('Nao existe ou e zero ou vazio...')