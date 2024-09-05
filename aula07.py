nome = ['jona', 'quadrado','cabecudo','negueba']

for i, j in enumerate(nome):  #enumerate chama os indices da lista colocando na variavel i e o j direcionando para a lista nome
    print(f'{i+1}º {j}')   #indice somado com 1 para começar do numero 1 e n do 0

nome1 = 'jona'
for x in nome1:  #ele ira executar x vezes e esse numero vai ser o tanto de letras que houver no nome
    print(x)

'''
for n in range(inicio, fim, interação):  #o range funciona com um intervalo numerico
    print(n)
    '''
  #contando de 0 a 10
for n in range(0, 10 +1):  # soma 1 na interação pois se colocar 10 ele vai ate la e só conta o 9, assim parando no 10
    print(n)  


# vendo se a divisao de um numero é exata e pedindo para imprimir o numero q o resto é 0

for u in range(0, 21):
    if u % 2 == 0:       # para saber se é impar usa-se o sinal de diferente de 0, o sinal é !=
        print(u)

#from vc chama uma biblioteca e dps vc passa o import para escolher oq vc quer chamar da biblioteca
'''
from time import sleep
'''
import os
from time import sleep
for k in range(5, -1, -1):
    os.system('cls')
    print(f'contando...{k}')
    sleep(1)
   
print('fim da contagem')