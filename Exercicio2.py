produtos = {}
def cadastra_produto():
    codigo = input ("Digite o codigo do produto: ")
    nome = input ("Digite o nome do produto: ")
    preco = float(input ("Digite o preço de venda: "))
    quantidade = int(input ("Digite a quantidade em estoque: "))
    produtos[codigo] = {"nome" : nome, "preço" : preco, "estoque" : quantidade}
    print("Produto adicionado com sucesso!")

def altera_preco():
    novo_preco = float(input("Digite o novo preço: "))
    codigo = input("Entre com o codigo do produto: ")
    if(codigo in produtos):
        produtos[codigo]["preco"] = novo_preco
        print("Preço alterado!")
    
def pesquisa_produto():
    codigop = input ("Digite o codigo do produto: ")
    produtoencontrado = produtos.get(codigop)
    if produtoencontrado:
        print("Produto encontrado")
        print(produtoencontrado)
    
while(True):
    print("\n=== Menu ===")
    print("1 - Adicionar produto")
    print("2 - Alterar o preço do produto")
    print("3 - Pesquisar por Código")
    print("4 - sair")
    print("-------------------------------")
    opcao = int(input("Escolha uma Opção: "))
    if (opcao == 1):
        cadastra_produto()
    elif(opcao == 2):
        altera_preco()
    elif(opcao == 3):
        pesquisa_produto()
    elif(opcao == 4):
        break
    else:
        print("Escolha a opção correta")