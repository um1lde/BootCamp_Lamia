

pessoas = ['Gui', 'Rebeca']
adj = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adj:
        print(f"{p} e {a}!")

for i in [1,2,3]:
    pass
# classe vaiza

for i in range(1,11):
    if i %2:
        continue
    print(i, end= " ")

print("\n")

for i in range(1,11):
    if i == 5:
        break
    print(i, end=' ')

print("\n")

print("Fim!")