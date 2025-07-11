# MongoDb e a Modelagem de banco documental
 
# Introdução - O que é o MongoDB?
 
Nesse tópico vamos começar a nos aprofundar em banco de dados não relacionais, para isso vamos utilizar o mongoDB.
 
MongoDB é um banco de dados que utiliza a estrutura orientada a documentos.
 
A seguir vamos entender um pouco mais sobre a sua estrutura.
 
# Modelagem de banco documental
 
Um banco de dados documental é um tipo de banco Não relacional, que armazena e consulta seus dados em documentos, no MongoDB os dados são salvos em documentos do tipo JSON.
 
Como vimos no tópico anterior, um banco não relacional não utiliza de tabelas com linhas em colunas, é comum em um banco relacional, termos diversas tabelas que se relacionam entre si e precisamos consultar, diversas tabelas para termos uma informação completa, como, por exemplo, uma tabela cliente que possui uma referência para tabela endereço e telefones com a finalidade de associar um cliente com diversos endereços e telefones que ele possa ter.
 
Em um banco não relacional todas essas informações ficariam concentradas em um único documento, um banco de dados não relacional é flexível e permite que esse documento possa crescer e ser incrementado conforme a evolução do sistema.
 
No MongoDB um conjunto de documentos são chamados de “Coleções” (collections) e essas coleções ficam salvas dentro de databases no mesmo banco.
 
Veja a seguir a estrutura de um um documento do salvo no MongoDb
 
````json
{
  "_id": "5cf0029caff7546b1ce7d",
  "nome": "Maria",
  "Sobrenome": "Silva",
  "endereco": {
    "rua": "rua dos sonhos",
    "cidade": "São Paulo",
    "Estado": "SP",
    "cep": "765445",
    "numero": 2
  },
  "telefones": [3434434,4343443,3434656]
}
````
 
## Algumas características do mongoDB
 
- Armazena dados do tipo JSON flexíveis;
- Não relacional;
- Escrito em C++;
- código aberto.
 
## Conclusão
 
Vimos até aqui algumas características do MongoDB e aprendemos sobre a sua modelagem. Uma modelagem documental, onde os seus documentos são em formato JSON flexíveis, ou seja, a sua estrutura pode ser modificada ao decorrer do projeto, os campos podem variar de documento para documento.
 
## Referências e indicações
[O que é o MongoDB?](https://www.mongodb.com/pt-br/what-is-mongodb). MongoDB. Acesso em: 02/07/2022.
 
[O banco de dados de documentos definido](https://aws.amazon.com/pt/nosql/document/). Amazon. Acesso em: 02/07/2022.
 
[Introdução ao MongoDB](https://www.devmedia.com.br/introducao-ao-mongodb/30792#:~:text=O%20MongoDB%20%C3%A9%20um%20banco,que%20seguem%20o%20modelo%20relacional.). Devmedia. Acesso em: 02/07/2022.
 
**Livros:**
 
[David Hows, Peter Membrey, Eelco Plugge · 2015. Introdução ao MongoDB](https://www.google.com.br/books/edition/Introdu%C3%A7%C3%A3o_ao_MongoDB/fw7vBgAAQBAJ?hl=pt-BR&gbpv=0)
 
[Shannon Bradshaw, Eoin Brazil, Kristina Chodorow · 2019. MongoDB: The Definitive Guide, 3rd Edition](https://www.oreilly.com/library/view/mongodb-the-definitive/9781491954454/)
