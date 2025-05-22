# Criando uma tupla de exemplo
minha_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Tupla:", minha_tupla)
print("Tupla[0]:", minha_tupla[0])
print("Tupla[-1]:", minha_tupla[-1])

try:
    minha_tupla[4] = 4
except TypeError:
    print("Não dá para modificar a tupla")

contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Indice da primeira ocorrência do elemento 3:", indice)