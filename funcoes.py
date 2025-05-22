def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("Guilherme")
saudacao("Fernando")
saudacao("Watyson")
saudacao("Marcio")


def quadrado(numero):
    return numero ** 2


resultado = quadrado(5)
print("Quadrado:", resultado)


def soma(num1, num2):
    return num1 + num2

num1 = 20
num2 = 50
print(f"Soma de {num1} e {num2} é igual a {soma(num1, num2)}")
