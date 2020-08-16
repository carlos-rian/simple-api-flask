ceps = [
    "06755962",
    828459,
    "9294510",
    "101011",
    1121112,
    122213,
    "55875648",
    1321314,
    "142415",
    1521516,
    "161617",
    172718,
    "05554865",
    "2584884",
    25876954,
]

for cep in ceps:
    cep = str(cep)
    tamanho = len(cep)
    if tamanho < 8:
        qtde_faltante_de_zeros = 8 - tamanho
        cep_corrigido = f"{qtde_faltante_de_zeros * '0'}{cep}"
        print(cep_corrigido)
    else:
        print(cep)
        
