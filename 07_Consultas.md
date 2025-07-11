# Consultas
 
## Introdução

Neste tópico vamos aprender algumas consultas que podemos realizar utilizando o MongoDB.
 
## Consultas básicas
 
Como já vimos, podemos utilizar o comando a seguir para trazer todos os dados de uma coleção.
 
````mongodb-json-query
 db.getCollection("alunos").find({})
````
 
ou
 
````mongodb-json-query
db.alunos.find()
````
 
Podemos utilizar o comando a seguir para contar todos os documentos de uma __collection__:
 
````mongodb-json-query
db.alunos.count()
````
 
Podemos realizar essa contagem passando alguma condição, como por exemplo, contar todos os documentos que o nome seja Joana:
 
````mongodb-json-query
db.alunos.count({nome: 'Joana'})
````
 
Para buscar dados com uma condição, por exemplo, buscar todos
os alunos que têm o curso Banco de dados:
 
````mongodb-json-query
db.alunos.find({curso: 'Banco de dados'})
````
 
## Operadores
 
Buscar dados que um determinado campo tenha qualquer um dos valores especificados, para isso utilizamos o ``$in``:
 
````mongodb-json-query
db.alunos.find({idade: {$in:[30,25]}})
````
 
Buscar alunos com menos de 30 anos, para isso utilizamos o ``$lt``:
 
````mongodb-json-query
 db.alunos.find({idade: {$lt:30}})
````
 
Buscar alunos que curso banco de dados e tem 40 anos:
 
````mongodb-json-query
db.alunos.find({idade:40, curso:"Banco de dados"})
````
 
 
Buscar alunos que cursam banco de dados ou tenham 25 anos:
 
````mongodb-json-query
    db.alunos.find({
      $or: [{idade:25},{curso:"Banco de dados"}]
    })
````
 
## Conclusão
 
Nesse tópico aprendemos a fazer algumas consultas diferentes e utilizando alguns operadores para criar condições.
 
## Referências e indicações
[Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/). MongoDB. Acesso em: 06/07/2022.
 
[$in](https://www.mongodb.com/docs/manual/reference/operator/query/in/). MongoDB. Acesso em: 06/07/2022.
 
Kamila Peres. [As diferenças entre SQL e NoSQL](https://www.letscode.com.br/blog/as-diferencas-entre-sql-e-nosql). Let's Code, 05/04/2021. Acesso em: 06/07/2022.
