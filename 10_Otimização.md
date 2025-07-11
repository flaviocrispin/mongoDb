# Otimização
 
## Introdução
 
Nesse tópico vamos aprender como otimizar e acelerar as buscas do nosso banco de dados com índices.
 
## Índice
 
### O que são?
 
São estruturas que armazenam um pequeno conjunto de dados de uma coleção de uma forma que permite que o banco de dados percorra de uma forma fácil e mais rápida.
 
O índice armazena de forma ordenada o valor de um campo específico ou de um conjunto de campos, isso permite que os dados sejam encontrados mais rápido sem a necessidade de percorrer uma coleção inteira.
 
### Utilização
 
Um índice é utilizado para auxiliar para buscas em um banco de dados, melhorar e acelerar o desempenho de uma busca. Com a existência de um índice apropriado, o banco de dados pode o utilizar para limitar o número de documentos que deve fazer a busca, sem isso o banco de dados irá fazer uma busca completa em todos os dados.
 
Veja a imagem a seguir que mostra como uma consulta é feita usando um índice:
 
![Consulta com indice](https://www.mongodb.com/docs/manual/images/index-for-sort.bakedsvg.svg)
 
**Figura 1** – Consulta é feita usando um índice (Fonte da imagem: [MongoDB](https://www.mongodb.com/docs/manual/indexes/))
 
Os índices do MongoDB são semelhantes aos índices de banco de dados relacional, como não temos tabelas no MongoDB, os índices são definidos no nível de coleção e podem ser criados índices em qualquer campo ou subcampo.
 
## Criando um índice
 
````mongodb-json-query
     db.alunos.createIndex( { nome: -1 } )
````
 
Especificamos o campo que queremos criar o índice, no caso nome e a ordem dele 1 - crescente e -1 decrescente.
 
Podemos criar um índice que corresponde a dois campos, como no exemplo a seguir:
 
````mongodb-json-query
 db.alunos.createIndex( { nome: -1, curso: 1} )
````
 
Dessa forma, quando fizermos a busca a seguir, nosso mongo não irá procurar em todos os campos do banco, ele irá utilizar o índice criado.
 
````mongodb-json-query
db.alunos.find({ nome: "Mariana", curso: "Banco de dados" })
````
 
## Alguns Tipos de índices
 
- _Single Field_: índices com classificação crescente e decrescente, os dados relacionados a esse índice são armazenados em uma ordem e podem ser classificados em crescente e decrescente;
- _Compound Index_: Criação de índices com múltiplos campos, ou seja, pode-se armazenar o valor de mais de um campo;
- _Multikey Index_: Utilizado para armazenar o conteúdo de um campo que seja do tipo array;
- _Geospatial Index_: índice utilizado para armazenar valores referentes a dados de informações geográficas;
- _Text Indexes_: índice utilizado para auxiliar na busca em valores de campos do tipo string;
- _Hashed Indexes_: O índice com hash, indexa o hash do valor de um campo.
 
## Índices eficientes
 
Vimos que índices são um recurso poderoso que podem nos ajudar muito em relação a performance do nosso banco de dados, mas isso significa que devemos criar índices para tudo?
 
A resposta para isso é, não. índices são estruturas de dados auxiliares, criadas para ajudar nas buscas e consomem espaço em disco, por isso temos que ter cuidado ao criá-los.
 
Ao criar um índice, é armazenado um valor e precisamos ter uma manutenção, se um índice é criado para uma coleção que tem muita alteração como _insert_, update e delete, precisaremos manter uma manutenção constante do índice e muito recurso do banco acaba sendo utilizado para manter aquele índice atualizado, se muitos índices que não são utilizados são criados e demandam muito recurso para sua manutenção forem criados, podemos piorar a performance no lugar de melhorá-la.
 
Índices são recursos poderosos, mas que precisamos ter cuidados no momento de criá-los.
 
## Conclusão
 
Agora podemos utilizar índices para otimizar e acelerar nossas buscas no banco de dados, trazendo muito mais performance para aplicação onde iremos utilizar o banco de dados.
 
## Referências e indicações
 
[Indexes](https://www.mongodb.com/docs/manual/indexes/). MongoDB. Acesso em: 12/07/2022.
 
[Índices](http://pgdocptbr.sourceforge.net/pg80/indexes.html). PostgreSQL. Acesso em: 12/07/2022.
 
 
 
 

