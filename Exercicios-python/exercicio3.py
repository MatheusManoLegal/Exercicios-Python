# Leitura de todas as notas
notas = []
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Cálculo das médias
media = sum(notas) / len(notas)

# Mostrar media na tela
print("Notas informadas:")
for i in range(4):
    print(f"Nota {i+1}: {notas[i]}")
print(f"Média: {media:.2f}")  # Utilizamos o formato de duas casas decimais na média
