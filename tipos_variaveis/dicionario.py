pessoa = {
    "nome": "Guilherme Henrique",
    "idade": 26,
    "cidade": "Goiânia"
}

print("Meu dicionário de pessoa:", pessoa)

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

try:
    print("Sobrenome:", pessoa["sobrenome"])
except KeyError:
    print("Chave não existe!")

pessoa["sobrenome"] = "Mendonça Nascente"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade:", pessoa["idade"])

print("Antes de deletar", pessoa)
del pessoa["sobrenome"]
print("Depois de deletar", pessoa)

# Metodos: keys(), values(), items()
chaves = pessoa.keys()
print("Chaves do dicionário:", chaves)

try:
    print("Primeira chave:", chaves[0])
except TypeError:
    print("Não tem como acessar pelo index")

chaves = list(pessoa.keys())
print("Primeira chave:", chaves[0])

valores = pessoa.values()
print("Valores:", valores)

valores = list(pessoa.values())
print("Valores (lista):", valores)
print("Primeiro valor:", valores[0])


itens = pessoa.items()
print("Conjunto de chave-valor como tupla:", itens)

itens = list(pessoa.items())
print(f"Primeira chave-valor: {itens[0][0]} = {itens[0][1]}")