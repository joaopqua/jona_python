import random 
import time
#recebe um numero aleatorio entre 0 e 100
num = random.randint(0,100)
contador = 0 
contador2 = []
tempo = 30

while True:
    ent_usuario = int(input('digite um numero de 0 a 100: '))
 
    if ent_usuario == num:
        print(60*'_')
        print('voce ganhou!!')
        print(f'os numeros tentados foram {contador2}')
        print(f'voce precisou de {contador} tentativas')
        print(60*'_')
        break
    else:
        #verifica se o numero e maior ou menor
        if ent_usuario > num:
            print('o numero sorteado é menor')
        else:
            print('o numero sorteado é maior ')
        print('que pena voce perdeu!!')
        print(40*'_')
        print('tente novamente')
        print(40*'_')
        #analisa quantas tentativas e os numeros tentados
        contador += 1
        contador2.append(ent_usuario)
