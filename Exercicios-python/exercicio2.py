vetor = []
for i in range(10):
    num = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(num)

# Impressão do vetor na ordem inversa
print("Vetor na ordem inversa:")
for i in range(9, -1, -1):
    print(vetor[i])