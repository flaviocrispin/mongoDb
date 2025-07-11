# Aprimorando consultas
 
## Introdução
 
Nesse tópico vamos aprender como aprimorar as nossas consultas utilizando algumas funções e operadores.
 
## Aggregation
 
A função ``aggregation`` são funções que agrupam dados e retornam um único resultado.
 
Vamos a um exemplo, queremos saber quais os cursos nossos alunos estão, invés de utilizar o ``find`` e olhar um por um, podemos utilizar o ``aggregate`` para agrupar os dados de curso e nos retornar uma lista com os cursos.
 
### $group
````mongodb-json-query
  db.alunos.aggregate([{
      $group:{_id:"$curso"}
  }])
````
 
Utilizamos o aggregate, passando um ``group`` que se refere ao que vamos agrupar e um _id_ onde passamos o nome do campo que queremos agrupar, o resultado deve ser como o seguinte:
 
 
![Resultado Aggregate](https://s3-sa-east-1.amazonaws.com/lcpi/e866f328-5eeb-4a8f-b317-4701a933132e.PNG)
 
**Figura 01** – Resultado Aggregate (Fonte da imagem: da autora)
 
No lugar de retornar esse resultado, podemos acrescentar um count, onde nos retornará também a quantidade de alunos em determinado curso
 
### $count e $sum
````mongodb-json-query
  db.alunos.aggregate([{
      $group:{
          _id:"$curso",
          count: {
            $sum: 1
            }
          }
  }])
````
 
Nesse comando passando o ``count`` que indicação que queremos contar e o ``sum`` onde dizemos que vamos fazer uma soma de 1 em 1.
 
Onde vamos ter um resultado como a seguir:
 
![Resultado Aggregate com count](https://s3-sa-east-1.amazonaws.com/lcpi/55558299-d3ca-4da1-8fc4-07ed45ded75f.PNG)
 
**Figura 02** – Resultado Aggregate com count (Fonte da imagem: da autora)
 
### $min
 
O ``$min`` agrupa por valor mínimo, por exemplo, se eu quiser saber qual a menor idade que eu tenho em cada curso.
 
````mongodb-json-query
  db.alunos.aggregate([{
  $group:{
    _id:"$curso",
    idadeMinima: {
      $min: "$idade"
    }
  }
}])
````
Resultado:
 
![Resultado Aggregate com $min](https://s3-sa-east-1.amazonaws.com/lcpi/b6fea53e-e317-481e-b386-21e7d9729e17.PNG)
 
**Figura 03** – Resultado Aggregate com $min (Fonte da imagem: da autora)
 
### $max
 
O ``$max`` agrupa por valor máximo, usando o mesmo exemplo anterior mas se agora eu quiser saber a idade
máxima de cada curso.
 
````mongodb-json-query
  db.alunos.aggregate([{
      $group:{
          _id:"$curso",
          idadeMinima: {
            $max: "$idade"
            }
          }
  }])
````
 
### $avg
 
Calcula o valor médio, podemos utilizar para calcular o valor médio de idade de aluno em cada curso:
 
````mongodb-json-query
  db.alunos.aggregate([{
      $group:{
          _id:"$curso",
          mediaDeIdade: {
            $avg: "$idade"
            }
          }
  }])
````
 
### $lookup
 
Executa associações com outras tabelas. Vamos ao exemplo, digamos que eu tenha uma _collection_ curso:
 
````mongodb-json-query
  db.createCollection("curso")
   db.curso.insertOne({
  nome: "dados",
  cargaHoraria: 40,
})
 
````
E na hora de buscar um aluno eu queira trazer junto as informações do curso:
 
````mongodb-json-query
  db.alunos.aggregate([{
  $lookup:{
    from: "curso",
    localField: "curso",
    foreignField: "nome",
    as: "curso_realizados"
  }
}])
````
 
Nesse comando eu digo de qual _collection_ eu quero pegar mais informações utilizando o ``from``:
 
- ``localField`` : o campo na _collection_ atual que eu vou usar de referência;
- ``foreignField``: o campo na _collection_ do from que eu vou comparar com o campo da tabela atual;
- ``as``: um nome para a junção desses dados.
 
O resultado será o seguinte:
 
````mongodb-json-query
{
    "_id" : ObjectId("62cd2b6dbf6c1286c81ab729"),
    "nome" : "Mariana",
    "sobrenome" : "Costa",
    "idade" : 25.0,
    "endereco" : {
        "rua" : "Avenida brasil 100",
        "cidade" : "são paulo",
        "estado" : "SP",
        "cep" : "54545"
    },
    "telefone" : [
        243443.0,
        2323.0,
        32323.0
    ],
    "curso" : "Banco de dados",
    "cpf" : 544545.0,
    "dataDeCriacao" : ISODate("2022-07-12T08:28:05.006+0000"),
    "curso_realizados" : [
        {
            "_id" : ObjectId("62cd461ebf6c1286c81ab735"),
            "nome" : "Banco de dados",
            "cargaHoraria" : 30.0
        }
    ]
}
{
    "_id" : ObjectId("62cd37d9bf6c1286c81ab72e"),
    "nome" : "Joana",
    "sobrenome" : "Silva",
    "idade" : 30.0,
    "curso" : "Banco de dados",
    "cpf" : 544545.0,
    "dataDeCriacao" : ISODate("2022-07-12T08:59:05.938+0000"),
    "curso_realizados" : [
        {
            "_id" : ObjectId("62cd461ebf6c1286c81ab735"),
            "nome" : "Banco de dados",
            "cargaHoraria" : 30.0
        }
    ]
}
````
 
### $unionWith
 
Executa uma união de duas coleções:
 
````mongodb-json-query
   db.alunos.aggregate([{
           $unionWith: { coll: "curso"}
   }])
````
 
Resultado:
````mongodb-json-query
{
    "_id" : ObjectId("62cd3dbdbf6c1286c81ab732"),
    "nome" : "Pedro",
    "sobrenome" : "Silva",
    "idade" : 40.0,
    "curso" : "Programação",
    "cpf" : 544545.0,
    "dataDeCriacao" : ISODate("2022-07-12T09:24:13.592+0000")
}
{
    "_id" : ObjectId("62cd4259bf6c1286c81ab733"),
    "nome" : "Pedro",
    "sobrenome" : "Silva",
    "idade" : 15.0,
    "curso" : "Programação",
    "cpf" : 544545.0,
    "dataDeCriacao" : ISODate("2022-07-12T09:43:53.294+0000")
}
{
    "_id" : ObjectId("62cd4613bf6c1286c81ab734"),
    "nome" : "Programação",
    "cargaHoraria" : 30.0
}
{
    "_id" : ObjectId("62cd461ebf6c1286c81ab735"),
    "nome" : "Banco de dados",
    "cargaHoraria" : 30.0
}
{
    "_id" : ObjectId("62cd4634bf6c1286c81ab736"),
    "nome" : "dados",
    "cargaHoraria" : 40.0
}
 
````
 
### Mais operadores
- ``$match``: Filtra os documentos para passar só os documentos correspondentes às condições especificadas;
- ``$sort``: Classifica os documentos em uma ordem especificada e os retorna;
- ``$limit``: Limita o número de documentos passados para o próximo passo;
- ``$skip``: Ignora documentos especificados e passo o restante para o próximo passo;
- ``$projet``: Passa os documentos e campos especificados para o próximo passo;
- ``$addFields``:  Adiciona novos campos aos documentos.
 
## Conclusão
 
Vimos diversas formas de aprimorar as nossas consultas utilizando algumas técnicas avançadas.
 
## Referências e indicações
 
[Aggregation Operations](https://www.mongodb.com/docs/manual/aggregation/). MongoDB. Acesso em: 12/07/2022.
 
[$min (aggregation)](https://www.mongodb.com/docs/manual/reference/operator/aggregation/min/). MongoDB. Acesso em: 12/07/2022.
 
[$avg (aggregation)](https://www.mongodb.com/docs/manual/reference/operator/aggregation/avg/). MongoDB. Acesso em: 12/07/2022.
 
[$lookup (aggregation)](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/). MongoDB. Acesso em: 12/07/2022.
 
[$unionWith (aggregation)](https://www.mongodb.com/docs/manual/reference/operator/aggregation/unionWith/). MongoDB. Acesso em: 11/07/2022.
