# Leitura dos caracteres
vetor = []
for i in range(10):
    char = input(f"Digite o {i+1}º caractere: ")
    vetor.append(char)

# Identificação das consoantes
consoantes = []
for char in vetor:
    if char.isalpha() and char.lower() not in 'aeiou':
        consoantes.append(char)

# Impressão das consoantes
print("Consoantes encontradas:")
for i in range(len(consoantes)):
    print(f"Consoante {i+1}: {consoantes[i]}")
print(f"Total de consoantes: {len(consoantes)}")
