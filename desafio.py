itens = []
total = []
while True:
    print(20*'_', 'menu da loja',20*'_')
    print('1. para adicionar um item ao catalogo')
    print('2. ver o valor total')
    print('3. listar os produtos')
    print('4. sair')
    print(52*'_')

    op = input('digite qual das opções vc quer realizar: ')

    if op == '1':
        nome = input('digite o nome do item q deseja adicionar: ')
        qtd = int(input('qual a quantidade do item: '))
        preco = float(input('qual o valor do item: '))
        t = qtd * preco
        total.append(t)
    elif op == '3':
        for i, n in enumerate(itens):
            print(f'{i + 1}º {n}')
    
    elif op == '2':
        print(f'o valor total das suas compras ate agora é de {sum(total)} reais')

    elif op == '4':
        print('lista finalizada, fim das compras')
        break