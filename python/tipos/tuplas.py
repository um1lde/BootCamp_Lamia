nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')
# pode se ter elementos repetidos dentro de uma tupla

print('Bia' in nomes)
# vai retornar true ou false se caso o nome estiver contido na tupla, isso funciona na lista tambem

print(nomes[0]) #voce ira acessar o elemento contido na posicao selecionada
print(nomes[1:2]) #voce ira acessar do primeiro elemento ate o segundo sem incluir o segundo 
print(nomes[1:-1])
print(nomes[1:])
print(nomes[:-2])


x =('Bia',) 
# se tiver apenas um nome entre aspas sera tipo string, se colocar virgula sera do tipo tupula
print(type(x))
print(type(nomes))
print("\n", nomes)