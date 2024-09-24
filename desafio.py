inventario_loja = []
precos = []
inv = []

while True:
    print( 30*'*', 'Inventario', 30*'*')
    print('1. Adicionar produto.')
    print('2. Atualizar quantidade de produtos.')
    print('3. Valor do estoque.')
    print('4. Produtos disponiveis.')
    print('5. Sair')
    print(66*'*')
    print()
    opcao = input('Digite a opção desejada: ')
    
# Adicionar produtos

    if opcao == '1':
        nome = input('digite o nome do produto: ')
        quantidade = int(input('digite a quantidade do produto: '))
        preco = float(input('digite o preco do produto: '))

        inventario_loja.append([nome, quantidade, preco])
        print(f'produto {nome} adicionado com sucesso')

# Atualizar a quantidade de produtos

    elif opcao == '2':
         nome = input('Digite o nome do produto que deseja atualizar: ')
         nova_quantidade = int(input('Digite a nova quantidade: '))

         encontrado = False

         for produto in inventario_loja:
             if produto[0] == nome:
                 produto[1] = nova_quantidade
                 print(f'Quantidade do produto {nome} atualizada para {nova_quantidade}.')
                 encontrado = True
                 break
             if not encontrado:
                 print(f'O produto {nome} não foi encontrado.')
# Valor do estoque

    elif opcao == '3':
        valor_total = 0
        for produto in inventario_loja:
            valor_total += produto[1] * produto[2]
        print(f'Valor toral do inventario é: R${valor_total:.2f}.')

# Listagem dos produtos

    elif opcao == '4':
        if len(inventario_loja) == 0:
            print('O inventario esta vazio!')
        else:
            print('Produtos no inventario:')
            for produto in inventario_loja:
                print(f'Nome: {produto[0]} | Quantidade: {produto[1]} | Preço: {produto[2]:.2f}.')

# Saida do sistema
 
    elif opcao == '5':
        print('Saindo do Sistema!')
        break
    else:
        print('Digite uma opcao válida: ')