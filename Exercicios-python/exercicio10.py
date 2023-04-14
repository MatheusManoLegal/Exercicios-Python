# Leitura dos elementos dos vetores A e B
vetor_A = []
vetor_B = []
for i in range(10):
    num_A = int(input(f"Digite o {i+1}º elemento do vetor A: "))
    vetor_A.append(num_A)
    num_B = int(input(f"Digite o {i+1}º elemento do vetor B: "))
    vetor_B.append(num_B)

# Geração do vetor C com os elementos intercalados dos vetores A e B
vetor_C = []
for i in range(10):
    vetor_C.append(vetor_A[i])
    vetor_C.append(vetor_B[i])

# Impressão do vetor C
print("Vetor A: ", vetor_A)
print("Vetor B: ", vetor_B)
print("Vetor C com elementos intercalados de A e B: ", vetor_C)
