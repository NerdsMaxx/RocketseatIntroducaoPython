minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo os elementos

# Alterando uma posição específica
minha_lista[0] = "python"
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]", minha_lista[1:7])
print("minha_lista[:6]", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])

# Métodos de lista

minha_lista.append(6)  # adiciona no final
print("Após append(6):", minha_lista)

indice = minha_lista.index(6)
print("Indice elemento 6:", indice)

minha_lista.insert(2, 10)  # adiciona um elemento na posição específica
print("Após o insert(2,10):", minha_lista)

elemento_removido = minha_lista.pop(6)  # removendo elemento da posição 6
print("Elemento removido:", elemento_removido)
print("Após pop(6):", minha_lista)

minha_lista.remove(True)  # remove um valor especifico dentro da lista
print("Após remove(True):", minha_lista)

minha_lista = [9, 4, 110, 3, 2, 10, 5, 6, 7, 8, 1]
minha_lista.sort()
print("sort:", minha_lista)
    