from functools import reduce

def somar_nota(delta):
    def calc(nota):
        return delta + nota
    return calc

notas = [6.4, 7.2, 5.4, 8.4]

# notas_finais = map(mais_um_meio, notas)
# notas_finais = map(somar_nota(1.5), notas)

notas_finais_1 = list(map(somar_nota(1.5), notas))
notas_finais_2 = list(map(somar_nota(1.6), notas))

# notas_finais = list(map(mais_um_meio, notas)) apenas deste jeito funcionou

print(notas_finais_1 ,notas_finais_2) # deu erro e nao consegui identificar, o gpt diz que precisamos converter o iterador em uma lista para podermos imprimir

'''
total = 0

for n in notas:
    total += n
    
print(total)
'''

def somar(a,b):
    return a + b 

total = reduce(somar,notas, 0) #pega uma lista percorre por todos os itens e ai chamando uma funcao, primeiro paramentro um acumulador e segundo

print(total)


# for i,nota in enumerate(notas):
#     notas[i] = nota + 1.5    
    
# for i in range(len((notas))):
#     notas[i] = notas[i] + 1.5    

# print(notas)