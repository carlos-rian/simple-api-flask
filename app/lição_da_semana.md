# lição da semana

Crie um novo banco de dados de item, semelhante ao de pessoas, no qual você irá fazer um CRUD completo com o banco de dados em memoria.
Use todo o conhecimento passado na última aula, por exemplo status code, methods, message etc, além disso considere sempre colocar nomes que fazem sentidos tanto nas funções quanto nos argumentos. Se atente há **sempre** retornar os dados no formato **JSON**.

``` yaml
C: CREATE -> POST
    - Crie um endpoint que irá receber os dados no 
    body como json e salve os dados no banco de item,
    o id do banco deve ser adicionado automaticamente e não pode se repetir. 
    Os dados recebidos devem ser validados antes de ser inseridos.

R: READ -> GET
    - Crie um endpoint que irá receber um id no path da url, o id não é obrigatório.
    Faça um filtro no banco e retorne o item caso o id seja encontrado.
    Caso o id informado não seja encontrado retorne uma mensagem de error com status de não encontrado.
    Caso o id não seja informado você deve retornar todos os itens do banco.

U: UPDATE -> PUT ou PATCH
    - Crie um endpoint que irá receber um id no path da url e os novos dados como json no body.
    Com o id você deve verificar se o cadastro existe, caso exista você deve fazer update com 
    os novos dados que foram enviados como json. 
    Não esqueça de validar os dados recebidos. Caso o id não exista retorne uma mensagem de erro informando. 

D: DELETE -> DELETE
    - Crie um endpoint que irá receber um id no path da url, verifique se o id existe, 
    caso exista remova o usuário e retorne uma mensagem informando que o usuário foi removido 
    e quais dados foram removidos. Caso não, retorne uma mensagem informando o erro.
```

Qual o formato dos dados que você deve inserir? Você deve validar e inserir os dados no formato json (dict) abaixo.

``` json
    {
        "prod": "Notebook i5 16gb de Ram 256 SSD",
        "qtde": 50,
        "preco": 2683.52,
        "marca": "Dell"
    }
```