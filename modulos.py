print("Exemplo de importação de um módulo padrão:")

# import math
from math import sqrt

# resultado: float = math.sqrt(2)
resultado: float = sqrt(2)
print(resultado)

import meu_modulo

print(meu_modulo.saudacao("Guilherme"))
print(meu_modulo.dobro(5))

from meu_modulo import dobro

print(dobro(10))