
participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

nome = input("Nome do participante a ser removido: ")
if nome in participantes["Workshop 1"] :
    participantes["Workshop 1"].discard(nome)
    print(f"Nome do participante removido: {nome}")
    print(f"lista atualizada dos participantes: {participantes}")
else:
    print("O nome desse participante não esta no dicionario")