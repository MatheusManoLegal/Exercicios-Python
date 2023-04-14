# Leitura das notas e cálculo da média
medias = []
for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

# Contagem de alunos com média maior ou igual a 7.0
num_alunos_aprovados = 0
for media in medias:
    if media >= 7.0:
        num_alunos_aprovados += 1

# Impressão do resultado
print("Médias dos alunos: ", medias)
print("Número de alunos com média maior ou igual a 7.0: ", num_alunos_aprovados)
