

class Produto:
    def __init__(self, nome, preco = 1.99, desc = 0): #instanciar um novo objeto
        self.nome = nome
        self.__preco = preco
        self.desc = desc
    
    @property # para ler
    def preco(self):
        return self.__preco
        # return f'R$ {self.__preco}'

    @preco.setter #decorator pra alterar
    def preco(self, novo_preco):

        if novo_preco > 0:
            self.__preco = novo_preco
        
    @property #faz com que preco_final seja entendido como uma variavel e nao como um metodo, portanto podemos retirar os ()
    def preco_final(self):
        return (1- self.desc) * self.preco

p1 = Produto('Caneta', 10, 0.1) # type: ignore
p2 = Produto('Caderno', 10, 0.2) # type: ignore

p1.preco = 70.89
p2.preco = 17.99

print(p1.nome, p1.preco, p1.desc, 'Preco com desconto', p1.preco_final)
print(p2.nome, p2.preco, p2.desc, 'Preco com desconto',p2.preco_final)