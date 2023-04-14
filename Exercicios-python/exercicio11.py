# Leitura dos elementos dos vetores A, B e C
vetor_A = []
vetor_B = []
vetor_C = []
for i in range(10):
    num_A = int(input(f"Digite o {i+1}º elemento do vetor A: "))
    vetor_A.append(num_A)
    num_B = int(input(f"Digite o {i+1}º elemento do vetor B: "))
    vetor_B.append(num_B)
    num_C = int(input(f"Digite o {i+1}º elemento do vetor C: "))
    vetor_C.append(num_C)

# Geração do vetor D com os elementos intercalados dos vetores A, B e C
vetor_D = []
for i in range(10):
    vetor_D.append(vetor_A[i])
    vetor_D.append(vetor_B[i])
    vetor_D.append(vetor_C[i])

# Impressão do vetor D
print("Vetor A: ", vetor_A)
print("Vetor B: ", vetor_B)
print("Vetor C: ", vetor_C)
print("Vetor D com elementos intercalados de A, B e C: ", vetor_D)
