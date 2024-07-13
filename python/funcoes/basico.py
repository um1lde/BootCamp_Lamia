
# def saudacao():
#     print("Bom dia")


# def saudacao(nome):
#     print(f"Bom dia {nome}")

def saudacao(nome = "Pessoa", idade = 20):
    print(f"Bom dia {nome}! Vc me, parece ter {idade} anos")
    # pass  
# toda funcao tem um bloco, por mais que a funcao nao faca nada voce tem que colocar um pass funcao vazia

print(__name__) # para acessar o nome do arquivo,  se executar o arquivo a partir daqui o nome sera __main__


if __name__ == '__main__':
    saudacao('Ana', idade= 30)

def soma_e_multi(a, b, x):
    return a + b * x
# podemos utilizar assim tbm