usuarios = {}
while True:
    print(30*'_','menu',30*'_')
    print('1. cadastrar usuario')
    print('2. listar usuario ')
    print('3. excluir usuario')
    print('4. inserir nome em uma posicao ')
    print('5. sair')
    print(60*'_')

    op = input('digite a opcao desejada: ')

    if op == '1':
        nome = input('digite o nome do usuario: ')
        email = input('digite o email do usuario: ')
        usuarios[nome] = {'nome' : nome, 'email' : email}
        print(f'usuario {nome} cadastrado com sucesso')

    elif op == '2':
        if usuarios:

            print('lista de usuarios')
            for email, dados in usuarios.items():
                print(f'nome: {dados['nome']} email: {dados['email']}')      

    elif op == '3':
        nome_remove = input('digite o nome que deseja deletar: ')
        if nome_remove in usuarios:
            del usuarios[nome_remove]
            print('usuario removido')

    elif op == '5':
        break