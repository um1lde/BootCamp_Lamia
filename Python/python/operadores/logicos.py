b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3)
# todos tem que ser verdadeiros para que seja True

print(b1 or b2 or b3)
# Or apenas um verdadeiro necessario para que todos sejam verdadeiros
print(b1 != b2) # equivalente ao xor 
print(not b1)
print(not b2)

print(b1 and not b2 and b3)

x = 3
y = 4

print(b1 and not b2 and x < y)