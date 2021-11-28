from Aula7_Televisao import Televisao
from Aula_7_Calculadora import Calculadora
from aula8_contador_letras import contador_letras, teste

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

calculadora = Calculadora(24, 8)
print(calculadora.soma())
print(calculadora.divisao())

lista = ['cachorro', 'gato', 'girafa', 'puma', 'elefante']
print(contador_letras(lista))
total_letras = contador_letras(lista)

print('O total de letras da lista é: {}' .format(total_letras))

print(teste())



