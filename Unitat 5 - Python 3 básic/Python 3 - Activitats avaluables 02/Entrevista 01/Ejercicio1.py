from functools import reduce


# lamba function
# We are taking the provided value and converting it into upper caps and printing the result
upper = lambda a: str.upper(a)
print(upper("cass"))


values = input("Enter numbers: ").split(" ")

# map(), list() and int() example
values = list(map(lambda x: int(x), values))

#Ejemplo filter
#Utilitzant “filter()”, elimina de la cadena anterior els números menors que 10.
print(values)
values = list(filter(lambda x : x >= 10, values))

#Ejemplo reduce
#Estamos realizando un cálculo acumulativo
suma = reduce(lambda x, y: x * y, values)
print(suma)