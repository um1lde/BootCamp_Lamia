a = 3
b = 4.4 

print(a +b)

texto = "Sua idade é..."
idade = 23

# print(texto + str (idade)) 
#conversao de uma variavel do tipo int para tipo string, porem nao é a melhor ao se fazer

print(f'{texto} {idade}') 
# f string, é utilizado para interpolar valores, lendo algo que está fora do texto e interpretar dentro do texto
# colocando entre chaves ele irá interpretar como código python

saudacao = 'bom dia \n'
print(3 * saudacao)

PI = 3.14
PI = 3.1415

raio = float (input('Informe o raio da circuferência: ')) 
# pelo resultado ser do tipo string, nos precisamos colocar no formato tipo float para tera precisao
area = PI * pow(raio, 2)


# print(type(raio)) 
# colocamos type dentro do print para obter o tipo daquela variavel no terminal

print(area)
print(f'A area da circuferência é = {area}')
