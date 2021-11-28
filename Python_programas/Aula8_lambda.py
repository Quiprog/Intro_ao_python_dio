contador_letras = lambda lista: [len (x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))


soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(24, 3))
print(subtracao(24, 8))


calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}


print(type(calculadora))

soma = calculadora['soma']
#soma = lambda a, b: a + b

divisao = calculadora['divisao']

print(soma(12, 3))
print(divisao(3, 12))