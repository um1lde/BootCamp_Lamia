
# comeca do 0 ate o 9 por padrao 
for i in range(10): 
    print(i)

print('\n')

for i in range(1, 11):
# ira comecar do 1 ate o 11, ou seja ira parar no 10
    print(i)

print('\n')

for i in range(1, 100, 7):
    # ira pular de 7 em 7 
    print(i)

print('\n')

for i in range(20, 0, -3):
    print(i)

print('\n')

nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=' ')

print('\n')

texto = 'Python e muito massa!'

for letra in texto:
    print(letra, end=' ')

print('\n')

for n in {1,2,3,4,4,4,}:
    print(n, end=' ')

print('\n')

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

for atrib in produto:
    print(atrib, '==>',produto[atrib])
print('\n')

for atrib, valor in produto.items():
    print(atrib, '==>',valor)

print('\n')

for valor in produto.values():
    print('==>',valor, end=' ')

print('\n')

for atrib in produto.keys():
    print('==>',atrib, end=' ')