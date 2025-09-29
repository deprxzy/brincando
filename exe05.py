
estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

nome = input("Digite o nome do produto a ser atualizado: ")
atualizar = int(input("Nova quantidade: "))
if nome in estoque.keys():
    estoque[nome]=atualizar
    print("Quantidade atualizada com sucesso!") 
else:
    print("Produto não encontrado no estoque.") 

print(estoque)

