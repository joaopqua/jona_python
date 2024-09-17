contador  =  0 
soma = 0
for i in range(1, 101):
    if i % 2 != 0:
        contador += 1   # toda vez q o for rodar ele vai somar 1 na variavel contador pois vai ter encontado mais um numero impar
        soma += i    # toda vez que o for rodar ele vai somar o valor de i na variavel soma

print(f'A soma dos numeros impares é: {soma}')
print(f'A quantidade de numeros impares é: {contador}')

