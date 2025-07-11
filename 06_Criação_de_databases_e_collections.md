# Criação de databases e collections
 
## Introdução
 
Com o nosso ambiente configurado, podemos começar a criação do nosso banco de dados (_database_) e coleções(_collections_), nesse tópico, vamos criar uma _database_ chamada letscode que tenha uma coleção para armazenar dados de alunos.
 
## Criando uma database
 
O primeiro passo para criar a _database_ e selecionar no Studio 3T a opção IntelliShell pois iremos realizar as criações por comando.
 
![IntelliShell](https://s3-sa-east-1.amazonaws.com/lcpi/0182abb7-7785-43bf-9711-38f6f0275777.PNG)
 
**Figura 01** – IntelliShell (Fonte da imagem: da autora)
 
Podemos utilizar o IntelliShell para executar comandos que vão interagir com o banco de dados, como, por exemplo, o comando ``show dbs`` que irá listar os bancos de dados que temos.
 
![Show dbs](https://s3-sa-east-1.amazonaws.com/lcpi/85c9fa6c-0576-4cc5-9769-616a18e69daf.PNG)
 
**Figura 02** – Show dbs (Fonte da imagem: da autora)
 
Como podemos ver, temos 4 bases de dados: _admin, config, local e testedb_.
 
Para criarmos a nossa base de dados, utilizamos o comando ``use``, onde indicaremos qual banco de dados vamos usar, caso ele não exista, o cluster do MongoDB irá criá-lo.
 
```mongodb-json-query
use letscode
```
 
Porém, se utilizarmos o comando ``show dbs`` novamente, podemos ver que o banco que foi criado não é listado, isso acontece porque um banco de dados não é totalmente criado até que seja inserido algo nele.
 
## Criando uma collection
 
Para criar um _collection_ podemos utilizar o comando a seguir:
 
````mongodb-json-query
    db.createCollection("alunos")
````
 
Perceba que a criação de uma _collection_ é diferente de criar uma tabela em um banco relacional, pois não precisamos passar dados de colunas e tipo de dados. Estamos trabalhando com um banco não relacional orientado a objetos e como já vimos o conteúdo de um documento, pode ser diferente de outro.
 
## Deletar collection
 
Para deletar uma _collection_ podemos utilizar o comando a seguir:
 
````mongodb-json-query
   db.collection.drop("alunos")
````
 
## Conclusão
 
Neste tópico aprendemos a criar um _database_ e _collections_, nós próximos passos vamos aprender a trabalhar com os dados.
 
## Referências e indicações
 
[Como criar um banco de dados com MongoDB](https://www.mongodb.com/pt-br/basics/create-database). MongoDB. Acesso em: 06/07/2022.
 
Kamila Peres. [As diferenças entre SQL e NoSQL](https://www.letscode.com.br/blog/as-diferencas-entre-sql-e-nosql). Let's Code, 05/04/2021. Acesso em: 06/07/2022.
