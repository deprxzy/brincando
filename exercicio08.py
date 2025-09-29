import os
import time

alunos = {
    "Maria": [5,6,5],
    "Pedro": [4,10,6]
    }



def menu():
    while True:
        print("==MENU==")
        print("1. CADASTRAR ALUNO")
        print("2. ADICIONAR NOTA")
        print("3. MOSTRAR BOLETIM DE TODOS OS ALUNOS")
        print("4. SAIR \n")
        
        opcao = int(input("Selecione a opção desejada: "))
        if opcao == 1:
            os.system("cls")
            cadastro_de_aluno()
        elif opcao == 2:
            os.system("cls")
            adicionar_nota()
        elif opcao == 3:
            mostrar_boletim()
        elif opcao == 4:
            os.system("cls")
            print("FINALIZANDO PROGRAMA")
            time.sleep(2)
            print("PROGRAMA FINALIZADO")
            break

def cadastro_de_aluno():
    while True:
        print("-- CADASTANDO UM ALUNO --\n")
        nome = input("Digite o nome do aluno que deseja cadastrar: ")
        if nome in alunos:
            print("Esse aluno ja foi cadastrado")
            time.sleep(2)
            os.system("cls")
            continue
        else: 
            alunos[nome] = []
            print("Aluno cadastrado com sucesso")
        desejo = input("Deseja cadastrar outro aluno? [S/N]: ").upper()
        if desejo == "N":
            break
            
def adicionar_nota():
    while True:
        print("== ADICIONAR NOTA DE ALUNO ==\n")
        nome = input("Digite o nome do aluno que deseja atribuir a nota: ")
        if nome in alunos:
            print(f"ADICIONANDO NOTA DO ALUNO - {nome} -")
            while len(alunos[nome]) < 3:
                nota = float(input("Digite uma nota: "))
                if nota < 0 or nota > 10:
                    print("A nota pode ser apenas maior que 10")                       vgf v       v      v    gvbv gv vgbvgb  vgb  vgbvgbgvgvb gvbgvb vgbgggggggggggggggggggggggggggggggggggggggggggvggbvgbgvf g fg fggf gfffffffffgg fg gggg  gg gf gf ff g gfg  fgf g fgf  fgff fggg fggggggffffffffffffffffffffffff fggg f gfffffffffffffffffffffffffffff gf gf fg fg g ffffff gtgtggggg ff fgg     cvvb vbn vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvnbbbbbbbbbnnnnn vn vbvb vb                   vb  vb vb   v vb         v b bv bbv                            
                    continue
                alunos[nome].append(nota)
            print(f"\nNotas do aluno {nome} registradas com sucesso!")
            break
        else:
            print("O nome deste aluno não existe no nosso banco de dados")
            time.sleep(2)
            os.system("cls")
        
def mostrar_boletim():
        print("-- MOSTRANDO BOLETIM DE TODOS OS ALUNOS --\n")
        while True:
            print("="*67)
            for nome, nota in alunos.items():
                media = sum(nota) / len(nota)
                situação = None
                if media >= 6:
                    situação = "Aprovado"
                else:
                    situação = "Reprovado"   
                       
                print(f"Aluno: {nome} | Notas: {nota} | Média {media:.2f} | Situação: {situação}")  
                
            print("="*67)    
            desejo = input("\nDeseja adicionar um novo aluno? [S/N]: \n").upper()
            if desejo == "S":
                time.sleep(1)
                os.system("cls")
                adicionar_nota()
            else:
                os.system("cls")
                break
                
            
            
    

if __name__ == "__main__":
    menu()
        
        