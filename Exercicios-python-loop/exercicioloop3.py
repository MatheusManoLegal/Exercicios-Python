while True:
    nome = input("Digite o nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    else:
        print("Erro: Nome deve ter mais de 3 caracteres. Tente novamente.")

while True:
    idade = int(input("Digite a idade (entre 0 e 150): "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("Erro: Idade deve estar entre 0 e 150. Tente novamente.")

while True:
    salario = float(input("Digite o salário (maior que zero): "))
    if salario > 0:
        break
    else:
        print("Erro: Salário deve ser maior que zero. Tente novamente.")

while True:
    sexo = input("Digite o sexo (f/m): ")
    if sexo.lower() == 'f' or sexo.lower() == 'm':
        break
    else:
        print("Erro: Sexo deve ser 'f' ou 'm'. Tente novamente.")

while True:
    estado_civil = input("Digite o estado civil (s/c/v/d): ")
    if estado_civil.lower() in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Erro: Estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente.")

print("Informações válidas:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
