

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

print(f"Largura: {retangulo.largura}")  
print(f"Altura: {retangulo.altura}")    
print(f"Área: {retangulo.area}")       
print(f"Perímetro: {retangulo.perimetro}")  


