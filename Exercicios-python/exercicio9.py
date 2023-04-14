# Leitura dos números inteiros
vetor_A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor_A.append(num)

# Cálculo da soma dos quadrados dos elementos do vetor
soma_quadrados = sum([num**2 for num in vetor_A])

# Impressão do resultado
print("Vetor A: ", vetor_A)
print("Soma dos quadrados dos elementos do vetor A: ", soma_quadrados)
