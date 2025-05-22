print("for lista")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elemento in lista:
    print(elemento, end=", ")

print("\nfor tupla")
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for elemento in tupla:
    print(elemento, end=", ")

pessoa = {"nome": "Guilherme", "idade": 26, "cidade": "Goiânia"}

print("\nFor utilizado dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("For utilizado dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("For utilizado dicionario - itens")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo numérico
print("range")
print(list(range(0, 10)))

print("For range")
for num in range(5):  # equivalente range(0,5)
    print(num, end=", ")

print("\n Utilizando range com len")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        print("Mudando para 100")
        lista[indice] = 100
    else:
        print("Mudando para 0")
        lista[indice] = 0
    print("Indice:", indice)
    print("Elemento:", lista[indice], "\n")


lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")