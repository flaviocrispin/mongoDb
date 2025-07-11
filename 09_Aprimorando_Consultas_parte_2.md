# Aprimorando consultas (parte 2)
 
## Introdução
 
Nesse tópico vamos aprender mais alguns operadores para aprimorar mais nossas consultas.
 
## Operadores aritméticos
 
### $add
Adiciona números ou adiciona números e uma data.
 
Adicionando 3 dias na data de criação:
 
````mongodb-json-query  
db.alunos.aggregate([{
$project: { nome: 1, data: { $add:["$dataDeCriacao", 3*24*60*60000]}}
}])
````
 
Resultado:
 
````mongodb-json-query
{
    "_id" : ObjectId("62cd2b6dbf6c1286c81ab729"),
    "nome" : "Mariana",
    "data" : ISODate("2022-07-12T08:28:05.009+0000")
}
{
    "_id" : ObjectId("62cd37d9bf6c1286c81ab72e"),
    "nome" : "Joana",
    "data" : ISODate("2022-07-12T08:59:05.941+0000")
}
````
 
### $subtract
 
Subtrair dois números ou duas datas para retornar a diferença:
 
````mongodb-json-query
  db.alunos.aggregate(
   [
     { $project: {Diferençadata: { $subtract: [ new Date(), "$dataDeCriacao" ] } } }
   ]
)
````
 
### Mais operadores
 
- `$multiply`: multiplica os números e retorna o resultado;
- `$divide`: divide os números e retorna o resultado;
- `$floor`: retorna o maior inteiro menor ou igual ao número especificado;
- `$ceil`: retorna o menor inteiro maior ou igual ao número especificado.
 
 
## Operadores de condicionais
 
### $cond
 
Avalia uma expressão booleana para retornar uma das duas expressões de retorno especificadas.
 
````mongodb-json-query
db.alunos.aggregate([
    {
           $project:
           {
             nome: 1,
             idade:
               {
                 $cond: { if: { $gte: [ "$idade", 18 ] }, then: "maior de 18", else: "menor de 18" }
               }
           }
 
    }
])
````
 
Resultado:
 
````mongodb-json-query
{
  "_id" : ObjectId("62cd37e8bf6c1286c81ab72f"),
  "nome" : "João",
  "idade" : "maior de 18"
}
{
  "_id" : ObjectId("62cd53bdbf6c1286c81ab737"),
  "nome" : "Pedro",
  "idade" : "menor de 18"
}
````
 
### Mais operadores
 
- `$ifNull`: avalia expressões de entrada para valores nulos;
- `$switch`: Avalia uma série de expressões de caso. Quando encontra uma expressão que é avaliada como verdadeira.
 
## Consultas na base de dados utilizando operadores de array
 
### #size
Retorna o elemento que o tamanho do array corresponde a condição.
 
````mongodb-json-query
 db.alunos.find({ notas: { $size: 2 } })
````
 
### Mais operadores
 
- `$concatArrays`: Concatena arrays para retornar o array concatenado;
- `$filter`:Retorna um array com apenas os elementos que correspondem à condição;
- `$arrayToObject`: Converte um array em um único documento;
- `$map`: Aplica uma expressão a cada item em um array e retorna o array com os resultados aplicados;
- `$reduce`: Aplica uma expressão a cada elemento em um array e os combina em um único valor;
- `$slice`: especifica o número de elementos em um array para retornar na consulta;
- `$indexOfArray`: Pesquisa uma ocorrência de um valor informado em um array e retorna o índice do array.
 
## Consultas na base de dados utilizando operadores de data
 
- `$year`: Retorna o ano de uma data;
- `$week`: Retorna a semana de uma data;
- `$month`: Retorna o mês de uma data;
- `$hour`: Retorna a hora de uma data;
- `$toDate`: Converte um valor em uma data;
- `$minute`: Retorna o minuto de uma data;
- `$millisecond`: Retorna o milissegundo de uma data;
- `$dayOfMonth`: Retorna o dia do mês da data;
- `$dayOfWeek`: Retorna o dia da semana da data;
- `$dayOfYear`: Retorna o dia do ano de uma data;
- `$dateToString`: Converte data em string.
 
Exemplo:
 
````mongodb-json-query
db.alunos.aggregate([
    {
      $project:
         {
           year: { $year: "$dataDeCriacao" },
           month: { $month: "$dataDeCriacao" },
           day: { $dayOfMonth: "$dataDeCriacao" },
           hour: { $hour: "$dataDeCriacao" },
           minutes: { $minute: "$dataDeCriacao" },
           seconds: { $second: "$dataDeCriacao" },
           milliseconds: { $millisecond: "$dataDeCriacao" },
           dayOfYear: { $dayOfYear: "$dataDeCriacao" },
           dayOfWeek: { $dayOfWeek: "$dataDeCriacao" },
           week: { $week: "$dataDeCriacao" }
         }
    }
  ])
````
 
Resultado:
 
````mongodb-json-query
{
    "_id" : ObjectId("62cd37d9bf6c1286c81ab72e"),
    "year" : NumberInt(2022),
    "month" : NumberInt(7),
    "day" : NumberInt(12),
    "hour" : NumberInt(8),
    "minutes" : NumberInt(59),
    "seconds" : NumberInt(5),
    "milliseconds" : NumberInt(938),
    "dayOfYear" : NumberInt(193),
    "dayOfWeek" : NumberInt(3),
    "week" : NumberInt(28)
}
````
 
## Conclusão
 
Neste tópico nos aprofundamos em algumas consultas com operadores, tornando uma consulta mais completa e assertiva.
 
## Referências e indicações
 
[Aggregation Pipeline Operators](https://www.mongodb.com/docs/manual/reference/operator/aggregation/). MongoDB. Acesso em: 12/07/2022.
 
[Query and Projection Operators](https://www.mongodb.com/docs/manual/reference/operator/query/). MongoDB. Acesso em: 12/07/2022.
