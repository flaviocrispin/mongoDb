# Criação de CRUD
 
## Introdução
 
Nesse tópico vamos aprender como realizar CRUD(Create, Read, Update and Delete) no MongoDB utilizando a coleção de alunos.
 
## Inserindo documentos
 
Para inserir um documento na collection podemos fazer da seguinte forma:
 
````mongodb-json-query
 
    db.alunos.insertOne(
        {
            nome: "Mariana",
            sobrenome: "Costa",
            idade: 25,
            endereco:{
                rua: "Avenida brasil 100",
                cidade: "são paulo",
                estado:"SP",
                cep:"54545"
            },
            telefone: [243443, 2323, 32323],
            curso:"Banco de dados",
            cpf: 544545,
            dataDeCriacao: new Date()
        }
    )
````
 
Ao realizar um insert, um id randômico automaticamente é criado e exibido no Raw Shell Output:
 
````mongodb-json-query
{
  "acknowledged" : true,
  "insertedId" : ObjectId("62cd2b6dbf6c1286c81ab729")
}
````
 
Como sabemos, um documento pode ser diferente do outro, mesmo estando na mesma, collection, dessa forma, podemos inserir na mesma collection um novo documento em outro formato:
 
````mongodb-json-query
    db.alunos.insertOne(
        {
          nome: "Joana",
          sobrenome: "Silva",
          curso:"Banco de dados",
          cpf: 544545,
          dataDeCriacao: new Date()
        }
  )
````
 
## Atualizar documentos
 
Existem algumas formas de atualizarmos um documento de uma collection, podemos utilizar ``updatOne``que irá modificar apenas um documento, o primeiro que ele encontrar que atenda a condição passada, que seja a seguinte sintaxe
 
``
db.alunos.updateOne(<condição>,<daodos para atualizar>, <condição>)
``
Veja um exemplo a seguir:
````mongodb-json-query
    db.alunos.updateOne(
        {nome:"Joana"},
        {$set: {"curso": "Programação"}}
     )
````
 
Se quisermos ter uma certeza maior do que estamos modificando, podemos utilizar o ID único que é gerado como condição.
 
````mongodb-json-query
    db.alunos.updateOne(
        {_id:ObjectId("62cd2cabbf6c1286c81ab72a")},
        {$set: {"curso": "Programação web"}}
     )
````
 
Outra forma de fazer um update é atualizar todos os documentos encontrados para determinada condição, utilizando o ``updateMany``
 
````mongodb-json-query
     db.alunos.updateOne(
        {nome:"Mariana"},
      {$set: {"dataDeCriacao": new Date()}}
    )
````
 
## Deletar documentos
 
Da mesma forma que o update, no delete temos o ``deleteOne`` e ``deleteMany``, onde o primeiro deleta o primeiro registro que encontrar para aquela condição e o segundo, todos que encontrar para aquela condição.
 
- Delete One
````mongodb-json-query
  db.alunos.deleteOne({nome: "Joana"})
````
 
- Delete one com Id
````mongodb-json-query
 db.alunos.deleteOne({_id: ObjectId("62cd3169bf6c1286c81ab72b")})
````
 
- Delete Many
 
````mongodb-json-query
  db.alunos.deleteMany({nome: "Joana"})
````
 
## Buscando dados
 
Para buscarmos os dados de uma collection podemos utilizar o comando
 
 
````mongodb-json-query
db.getCollection("alunos").find({})
````
Você terá um retorno parecido com esse:
 
![Retorno consulta](https://s3-sa-east-1.amazonaws.com/lcpi/894ebd72-166a-4f02-9466-07301b53f5a7.PNG)
 
**Figura 01** – Retorno Consulta (Fonte da imagem: da autora)
 
## Conclusão
 
Neste tópico conseguimos criar um CRUD completo de alunos, no próximo tópico vamos ver mais algumas formas de consulta.
 
## Referências e indicações
[Update Documents](https://www.mongodb.com/docs/manual/tutorial/update-documents/#update-documents). MongoDB. Acesso em: 06/07/2022.
 
[Date()](https://www.mongodb.com/docs/manual/reference/method/Date/). MongoDB. Acesso em: 06/07/2022.
 
Kamila Peres. [As diferenças entre SQL e NoSQL](https://www.letscode.com.br/blog/as-diferencas-entre-sql-e-nosql). Let's Code, 05/04/2021. Acesso em: 06/07/2022.
