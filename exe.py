texto1 = "O sol brilha forte no céu azul"
texto2 = " O céu azul anuncia um dia de sol intenso" 

texto1 = set(texto1.split())
texto2 = set(texto2.split())
editado = texto1 & texto2

print(editado)