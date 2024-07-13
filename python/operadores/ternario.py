lockdown = False
grana = 30

status = 'Em casa' if lockdown and grana <= 100 else 'Uhuuu'

# ternario pois tem 3 partes quando verdadeiro, expressão logica e quando é falso

print(status)
print(f'o status e: {status}') # f string
