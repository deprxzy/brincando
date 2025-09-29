
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

equipe_c = equipe_a.union(equipe_b)

remover = input("tarefa a ser removida: ").lower()

if remover in equipe_c:
    equipe_c.remove(remover)

print(equipe_c)