print("Exemplo de while")
contador = 0

while contador < 5:
    print("Contagem:", contador)
    contador += 1

print("Programa finalizado\n")

contador = 0
while True:
    print("Contagem:", contador)
    contador += 1
    if contador == 5:
        print("Break")
        break
    
print("Programa finalizado")