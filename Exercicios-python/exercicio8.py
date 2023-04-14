# Leitura das idades e alturas
idades = []
alturas = []
for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1} em metros: "))
    idades.append(idade)
    alturas.append(altura)

# Impressão das idades e alturas na ordem inversa
print("Idades na ordem inversa: ", idades[::-1])
print("Alturas na ordem inversa: ", alturas[::-1])
