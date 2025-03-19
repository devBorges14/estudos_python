#1 - Crie uma função lambda que receba um número e retorne o dobro dele.
import random
num = random.randrange(1,10)
soma = lambda x: x * 2
print(f'Dobro do número: {soma(num)} Número original: {num}')

# 2 - Crie uma função lambda que diga se um número é par (True) ou ímpar (False).
par_impar = lambda x: x % 2 == 0 
print(par_impar(random.randrange(1,10)))

# 3 - Dada uma lista de tuplas com nome e idade, ordene por idade usando lambda e sorted().
pessoas = [("Ana", 25), ("Bruno", 20), ("Carlos", 30)]
ordenado = sorted(pessoas, key=lambda pessoa: pessoa[1])
print(ordenado)

# 4 - Use lambda e filter() para filtrar os números maiores que 10 de uma lista.
"""
Modo que eu fiz (Funcionou)
separador = lambda num: num > 10
filter = list(filter(separador, lista))
"""
lista = [1, 2, 4,6, 11, 10, 112, 15]
maior_10 = list(filter(lambda num: num > 10, lista))
print(maior_10)

# 5 - Dadas duas listas de números, use lambda e map() para somá-las elemento por elemento.
lista_1 = [4, 5, 67, 22, 30]
lista_2 = [6, 12, 76, 44, 2]

soma = list(map(lambda x, y: x + y, lista_1, lista_2))
print(soma)
