unidades = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

def converter(quantidade, unidade_origem, unidade_destino):
    valores_em_bytes = {
        "bit": 0.125,
        "byte": 1,
        "KB": 1024,
        "MB": 1024 ** 2,
        "GB": 1024 ** 3,
        "TB": 1024 ** 4,
        "PB": 1024 ** 5
    }
    bytes_origem = quantidade * valores_em_bytes[unidade_origem]
    bytes_destino = valores_em_bytes[unidade_destino]
    quantidade_destino = bytes_origem / bytes_destino
    return quantidade_destino

quantidade = int(input("Digite a quantidade a ser convertida: "))
unidade_origem = input("Digite a unidade de origem: ")
unidade_destino = input("Digite a unidade de destino: ")
quantidade_convertida = converter(quantidade, unidade_origem, unidade_destino)
print(f"{quantidade} {unidade_origem} = {quantidade_convertida} {unidade_destino}")
