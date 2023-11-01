from aula7televisao import Televisao
from aula7calculadora1 import Calculadora
from aula8contadordeletras import contador_letras

televisao = Televisao ()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora(5, 10)
print(calculadora.soma())
lista = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista))
