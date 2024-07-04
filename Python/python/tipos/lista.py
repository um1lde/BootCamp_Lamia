
nums = [1,2,3]
# tipo lista o nums
print(type(nums))

nums.append(3)
# para adicionar mais um elemento na lista utilizamos o codigo acima num.append
nums.append(4)
# lista aceita numeros repetidos 
nums.append(500)
print(len(nums), "quantidade de indices\n")
# len serve para ver o tamanho da lista

nums[3] = 100
# nums[3] serve para alterar certo indice da lista 
nums.insert(0, -200)
# insert vai inserir um indice e desloca o resto para depois

print(nums[6], "Imprimindo o indice 6 da lista\n")

print(nums[-2], "Imprimindo o indice -2 ou seja o 5 da lista\n")

# se colocarmos o -1 pegara o ultimo elemento, ele identifica como se voce estivesse vindo de tras para frente 
# vai acessar o ultimo elemento do indice 
print(nums, "A lista e seus indices\n")