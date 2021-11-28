# for i in range(0, 51):
#     par = i % 2
#     if par == 0:
#         print(i, end='..')

# soma = 0
# for i in range(0, 501):
#     par = i % 3
#     if par == 0:
#         soma += i
#
# print(soma)

# num = int(input('Entre com um número para ver sua tabuada: '))
#
# for i in range (1, 11):
#         print('{:2} x {:2} = '.format(i, num), i * num)

#Desenvolva um programa que leia os seis números inteiros e mostre a soma apenas daqueles que são
# pares. Se o valor inteiro for ímpar, desconsidere-o.

# par1 = int(input('Entre com o primeiro número: '))
# while par1 % 2 != 0:
#     par1 = int(input('Você digitou um número. Entre com um número par: '))
# par2 = int(input('Entre com o segundo número: '))
# while par2 % 2 != 0:
#     par2 = int(input('Você digitou um número. Entre com um número par: '))
# par3 = int(input('Entre com o terceiro número: '))
# while par3 % 2 != 0:
#     par3 = int(input('Você digitou um número. Entre com um número par: '))
# par4 = int(input('Entre com o quarto número: '))
# while par4 % 2 != 0:
#     par4 = int(input('Você digitou um número. Entre com um número par: '))
# par5 = int(input('Entre com o quinto número: '))
# while par5 % 2 != 0:
#     par5 = int(input('Você digitou um número. Entre com um número par: '))
# par6 = int(input('Entre com o sexto número: '))
# while par6 % 2 != 0:
#     par6 = int(input('Você digitou um número. Entre com um número par: '))

# soma = 0
# cont = 0
# for i in range(1, 7):
#     a = int(input('Entre com um número: '))
#     if a % 2 == 0:
#         soma += a
#         cont += 1
# print(cont)
# print(soma)


#Desenvolva um programa que leia o primeiro termo e a razão de um PA e que, no final, mostre os dez
#primeiros termos dessa progressão.

# equação da para: an = a1 + (n-1)r

# a1 = int(input('Entre com o primeiro termo da PA: '))
# r = int(input('Entre com a razão desta PA: '))
# n = 10
# an = r*n
#
# for r in range(a1, an+1, r):
#     print(r)

#Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo. Desconsidere os espaços.

# frase = str(input('Digite uma frase: ')).strip().upper()
# #strip tira espaços e upper leva as letras para MAIÚSCULA.
# palavras = frase.split()
#
# junto = ''.join(palavras)
#
# inverso = ''
#
# for letra in range(len(junto) - 1, -1, -1):
#
#     inverso += junto[letra]
#
# if inverso == junto:
#
#     print('Temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo!')

# lst = [10,20,30,'oi', 'teste']
# for abx in lst:
#     print(abx)

# nomes = ['Ana', 'Maria', 'Carla']
# for bbb in enumerate(nomes):
#     print(bbb)

# nomes = ['Ana', 'Maria', 'Carla']
# for cc, ddd in enumerate(nomes):
#     print(cc, ddd)
