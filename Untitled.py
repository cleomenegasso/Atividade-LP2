#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy 

print(f"{'Calculadora estatística':^50}") 

quantidadeNum = int(input("Insira quantos números serão pedidos: "))
my_list = []

#loop que cria uma lista através da quantidade de números pedida.

for _ in range(quantidadeNum):
    try:
        my_list.append(float(input('Insira um número: ')))#aceita números do tipo float.
    except ValueError:
        print('O valor fornecido não é do tipo float')
    continue
numpy.asarray(my_list)#Converte a lista para um array
print(my_list)

opcao = 0

while opcao != 4:
  
    print('''Operações: 
    [1] - Média
    [2] - Mediana
    [3] - Variância
    [4] - Encerrar calculadora''')

    opcao = int(input("Sua opção: "))

    if opcao == 1:
        media = numpy.mean(my_list)
        print(media)

    elif opcao == 2:
        mediana = numpy.median(my_list) 
        print(mediana)

    elif opcao == 3:
        maximo = numpy.max(my_list)
        minimo = numpy.min(my_list)
        variancia = maximo - minimo
        print(variancia)
    
    else:
        print("Opcão inválida")

print("Calculadora encerrada!")

