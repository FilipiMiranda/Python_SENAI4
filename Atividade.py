aluno = {}

def cadastra_aluno():
    rn = input("Digite o Numero de Matricula: ")
    nome = input ("Digite o Nome do Aluno: ")
    data_nasc = input ("Digite a Data de Nascimento do Aluno: ")
    email = input ("Digite o Email do Aluno: ")
    telefone = int(input ("Digite o Telefone do Aluno: "))
    endereco = input("Digite o Endereço do Aluno: ")
    aluno[rn] = {"Nome" : nome, "Data de Nascimeto" : data_nasc, "Email" : email, "Telefone" : telefone, "Endereço" : endereco}
    print("Aluno registrado com sucesso!")
    
def pesquisar_aluno():
    rn = input ("Digite o Numero de Matricula: ")
    alunoencontrado = aluno.get(rn)
    if alunoencontrado:
        print("Aluno encontrado")
        print(alunoencontrado)

def alterar_endereco():
    novo_endereço = float(input("Digite o novo Endereço: "))
    rn = input("Entre com o Numero de Matricula: ")
    if(rn in aluno):
        aluno[rn]["Endereço"] = novo_endereço
        print("Endereço alterado!")

def liste_todos():
    print(aluno)

while(True):     
    print("\n=== Menu ===")
    print("1 - Cadastrar Aluno")
    print("2 - Pesquisar Aluno")
    print("3 - Liste todos os Alunos")
    print("4 - Alterar Endereço do Aluno")
    print("5 - sair")
    opcao = int(input("Escolha uma Opção: "))
    if (opcao == 1):
        cadastra_aluno()
    elif (opcao == 2):
        pesquisar_aluno()
    elif(opcao == 3):
        liste_todos()
    elif(opcao == 4):
        alterar_endereco()
    elif(opcao == 5):
        break
    else:
        print("Escolha a opção correta")
    