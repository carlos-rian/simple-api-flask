# Para ler um arquivo em python o mais indicado é usar o método open juntamente com a instrução
# With, o With é um gerenciado de contexto python. Ou seja, o with é responsável por abrir e fechar
# Uma sessão, sendo assim você não precisa se preocupar se um arquivo está ou não aberto.

""" 
    - with: irá criar uma sessão/contexto que ao final será fechado automaticamente.
    - open: irá abrir o arquivo.
        - file: É o argumento que irá receber o caminho onde está o arquivo que você irá ler.
        - mode: É o argumento que indentificar em qual modo você vai executar a abertura do 
            arquivo, podendo usar diversas combinações porém usaremos apenas essas três, 

            "r" abrir em modo de read(leitura) - Apenas ler o arquivo.
            "w" abrir em modo de write(escrita) - Cria um novo arquivo ou sobrescreve o antigo.
            "a" abrir em modo de append(adiciona) - Pode escrever novos dados no arquivo existente.

        - enconding: É o argumento que irá informar para o open qual o tipo de códificação ele deve usar
            para abrir esse arquivo. Neste caso "utf-8" 
    - as: É uma palavra reservada no python que usamos para dá apelido há algo, assim como no sql.
    - file: É a variável que iremos criar para receber "sessão"/"abertura" do arquivo.

    Somente em modo de escrita e adiciona:
        - texto: será o valor que será adicionado no arquivo.

"""

# 1 - Como ler um arquivo.
with open(file="coloque_aqui_o_caminho_do_arquivo.extenção", mode="r", encoding="utf-8") as file:
    ceps = file.read()

# 2 - Como escrever/sobrescrever um arquivo.
with open(file="coloque_aqui_o_caminho_do_arquivo.extenção", mode="w", encoding="utf-8") as file:
    texto = "este valor será criado no arquivo caso não exista ou sobrescrito caso exista"
    file.write(texto)

# 3 - Como adicionar um novo texto em um arquivo.
with open(file="coloque_aqui_o_caminho_do_arquivo.extenção", mode="a", encoding="utf-8") as file:
    texto = """
        este valor será adicionado na última linha do seu arquivo caso exista, 
        caso não exista será criado e adicionado.
    """
    file.write(texto)
