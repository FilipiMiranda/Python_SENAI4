produtos = {}

while True:
    codigo = input ("Digite o codigo do produto: ")
    nome = input ("Digite o nome do produto: ")
    preco = float(input ("Digite o preço de venda: "))
    quantidade = int(input ("Digite a quantidade em estoque: "))
    produtos[codigo] = {"nome" : nome, "preço" : preco, "quantidade" : quantidade}  
    print("Produto adicionado com sucesso!")
    print("\n=== Deseja Parar? ===")
    print("1 - Sim")
    print("2 - Não")    
    
    opcao = int(input("Escolha uma opcao: "))
    match opcao:
        case 1:
             
            print(produtos)
            break
            
        case 2: 
           
            continue
    
       

    