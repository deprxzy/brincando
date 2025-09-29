estoque = {
    
}
for i in range(3):
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    estoque[produto] = quantidade
    
print(estoque)