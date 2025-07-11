# Banco de dados Relacional x Não relacional
## Introdução
 
Nesse tópico vamos entender o que é banco de dados relacional, não relacional e responder
algumas perguntas sobre a diferença entre os dois.
 
## Relacional
Banco de dados relacionais, são estruturas que armazenam dados e fornecem acesso a dados
salvo em estrutura de tabelas, a princípio podemos compará-los como uma tabela do excel por exemplo,
onde cada linha representa um registro que possui um ID único e colunas referente aos demais dados.
Veja o exemplo a seguir:
 
![Tabela 1](https://s3-sa-east-1.amazonaws.com/lcpi/c3d5362d-b120-4c2b-bbf9-8c09d1c56d68.png)
 
**Figura 1** – Tabela 1 (Fonte da imagem: da autora)
 
Essas tabelas podem conter também relacionamentos entre sí, como no exemplo a seguir:
 
![Tabela 2](https://s3-sa-east-1.amazonaws.com/lcpi/1c8ed185-b744-42f3-872d-2364a530e5af.png)
 
**Figura 2** – Tabela 2 | Relacionamento (Fonte da imagem: da autora)
 
Podemos dizer então que um banco de dados relacional utiliza de um modelo relacional,
que é uma maneira de representar dados em tabelas.
 
## Não relacional
 
Um banco de dados não relacional são banco de dados que não utilizam de modelo relacional,
mas o que isso quer dizer? Esse tipo de banco de dados armazena dados de uma forma diferente dos
bancos relacionais, ou seja, ele não utiliza tabelas de linhas e colunas. A estrutura desse tipo
de banco de dados é criada para modelos de dados específicos. É um tipo de armazenamento otimizado. Os dados podem ser armazenados sem ser definido o esquema previamente.
 
Existem algumas formas utilizadas para definir a estrutura de um banco de dados não relacional,
como por exemplo: chave-valor, orientado a documentos, gráficos, etc.
 
Veja um exemplo de chave-valor e orientado a documentos que são duas formas muito utilizadas:
 
Chave-valor
 
![Estrutura chave-valor](https://s3-sa-east-1.amazonaws.com/lcpi/6a9f33a9-b331-425b-8fce-c69d71503b4f.png)
 
**Figura 3** – Estrutura Chave-valor (Fonte da imagem: da autora)
 
Orientada a documentos
 
![Estrutura orientada a documento](https://docs.microsoft.com/pt-BR/azure/architecture/data-guide/big-data/images/document.png)
 
**Figura 4** – Estrutura orientada a documento (Fonte da imagem: [Microsoft](https://docs.microsoft.com/pt-br/azure/architecture/data-guide/big-data/non-relational-data))
 
 
## Relacional x Não relacional
 
Agora que entendemos o que é um banco relacional e um não relacional, qual a diferença entre eles?
Um banco de dados relacional tem uma estrutura bem definida, onde precisamos ter uma definição da estrutura com antecedência.
Já com o banco de dados não relacional não temos essa necessidade o que significa que temos uma forma de se adaptar a
uma nova regra rapidamente. O grande diferencial de um banco não relacional é a sua capacidade de escalabilidade e com isso
lidar com um alto tráfego de dados.
 
## Conclusão
 
Existem diferentes formas de armazenar dados e cada um com sua vantagem, não significa que um seja melhor que o outro
mas para escolher uma dessas formas para o nosso projeto depende de qual irá se encaixar melhor de acordo com as regras
de negócio do sistema.
 
## Referências e indicações
 
[O que é NoSQL?](https://www.oracle.com/br/database/nosql/what-is-nosql/). Oracle. Acesso em: 02/07/2022.
 
Kamila Peres. [As diferenças entre SQL e NoSQL](https://www.letscode.com.br/blog/as-diferencas-entre-sql-e-nosql). Let's Code, 05/04/2021. Acesso em: 02/07/2022.
 
[O que são bancos de dados NoSQL?](https://aws.amazon.com/pt/nosql/). Amazon. Acesso em: 02/07/2022.
 
[Dados não relacionais e NoSQL](https://docs.microsoft.com/pt-br/azure/architecture/data-guide/big-data/non-relational-data). Microsoft. Acesso em: 02/07/2022.
 
**Livros:**
 
[Pramod J. Sadalage, Martin Fowler · 2013. NoSQL Essencial: Um Guia Conciso para o Mundo Emergente da Persistência Poliglota](https://www.google.com.br/books/edition/NoSQL_Essencial/m6jiDQAAQBAJ?hl=pt-BR&gbpv=0)
