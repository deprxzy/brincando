laura = set()
ana = set()

for i in range (0,3):
    pergunta = input("Lista de Laura: ").lower()
    laura.add(pergunta)

for i in range(0,3):
    pergunta = input("Lista de ana: ").lower()
    ana.add(pergunta)
        
print(f"Itens em ambas as listas: {laura.intersection(ana)}")
print(f"itens exclusivos da laura: {laura.difference(ana)}")
print(f"Itens exclusivos da ana: {ana.difference(laura)}")


