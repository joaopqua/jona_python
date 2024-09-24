alunos = {}

while True:
    print('1. calcular media do aluno')
    print('2. fechar sistema')
    print('3. visualizar a nota do aluno desejado')

    op = input('digite qual opcao vai usar: ')

    if op == '1':
        nome = input('digite o nome do aluno que quer cadastrar: ')
        n1 = float(input('digite a primeira nota do aluno: '))
        n2 = float(input('digite a segunda nota do aluno: '))
        n3 = float(input('digite a terceira nota do aluno: '))
        media = (n1 + n2 + n3) /3
        print(f'nome: {nome}, Média: {media:.2f}')
        alunos[nome] = {'nome' : nome, 'media' : media}

    
    elif op == '3':
        nome_visu = input('digite o nome que deseja visualizar: ')
        if nome_visu in alunos:
            print(alunos[nome_visu])
        else:
            print('o usuario nao foi encontrado')
    
    
    elif op == '2':
        break 