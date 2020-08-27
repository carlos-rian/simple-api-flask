texto_de_config = """
    cdvend={codigo}
    nomvend={vendedor} 
    numped={pedido}
    versis= 3.0.0.99
    ip=200.186.96.250
    porta= 3652
    hostsmtp=200.186.96.246
    portasmtp=25
    portapop=110
    usuemail=wconnect
    senhaemail=rb@14r7
    remetemailerr=sistemas@wurth.com.br
    destemailerr=fabio.veiga@wurth.com.br
    tempcomuni=0
    tempoversao=0
    tempoenviaemail=0
"""
print(type(texto_de_config))

vendedores = [
    {"cdvend": 123456, "nomvend": "João Paulo", "numped": 5,},
    {"cdvend": 654123, "nomvend": "Marcelo", "numped": 154,},
]

for vendedor in vendedores:
    texto = texto_de_config.format(codigo=vendedor["cdvend"], vendedor=vendedor["nomvend"], pedido=vendedor["numped"])
    print(texto)
