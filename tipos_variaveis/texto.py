nome_completo = 'Guilherme Henrique'

#pula linha na string
nome_completo_aspas = """Guilherme 
Henrique"""

#pula linha só no editor, na string fica só uma linha normal
nome_completo_quebra = "Guilherme \
Henrique"

#formatacao
print("nome_completo ", nome_completo)
print("nome_completo %s" % nome_completo)
print("nome_completo %s %s" % ("Guilherme", "Henrique"))
print("nome_completo_aspas " + nome_completo_aspas)
print("nome_completo_aspas " + "Guilherme", "Henrique")
print("nome_completo_quebra {}".format(nome_completo))
print(f"nome_completo_quebra {nome_completo_quebra}")