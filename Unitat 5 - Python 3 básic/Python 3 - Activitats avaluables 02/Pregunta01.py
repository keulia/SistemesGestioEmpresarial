from arepl_dump import dump
from functools import reduce

#Ejemplo map

#Ejemplo filter
#Utilitzant “filter()”, elimina de la cadena anterior els números menors que 10.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9,11,25]
print(valores)
impares = list(filter(lambda x : x >= 10, valores))
valores= impares

#Ejemplo reduce
#Estamos realizando un cálculo acumulativo
suma = reduce(lambda x, y: x * y, valores)
print(suma)