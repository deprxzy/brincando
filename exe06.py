
participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

print(f"Nome dos participantes: {participantes.keys()}")
print(f"Idade dos participantes: {participantes.values()}")

for nome, idade in participantes.items():
    print(f"- {nome}: {idade}")