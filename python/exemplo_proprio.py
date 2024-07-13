
#iremos criar uma class que ira receber a altura e largura e assim irá calcular area e o perimetro, logo em seguida iremos imprimir todos os valores calculados

class Retangulo:
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property #utilizei @property em todos pois acho que fica mais facil chamarmos como variavel e nao como metodo
    def area(self):
        return self.__largura * self.__altura #calculamos a area do retangulo 

    @property
    def perimetro(self):
        return 2 * (self.__largura + self.__altura) #calculamos o perimetro


retangulo = Retangulo(5, 10) #criamos uma instancia para o retangulo
    
print(f'Área: {retangulo.area}') #impressao dos calculos
print(f'Perímetro: {retangulo.perimetro}')  


