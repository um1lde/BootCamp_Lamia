

class Contador:
    contador = 0 #atributo de classe

    def inst(self):
        return 'Estou bem' 
    
    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    @staticmethod #metodo estatico nao precisa de uma instancia
    def mais_um(n):
        return n + 1

# c1 = Contador()
# print(c1.inst())
# print(Contador.inst()) # nao da pra acessar como uma classe precisaria de uma instancia


print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99))

# print(c1.inc())
# print(c1.inc())
# print(c1.inc())
# print(c1.dec())
# print(c1.dec())
# print(c1.dec())