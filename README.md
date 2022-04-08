# TechNews - Data Scraper ⛏️

Esse projeto tem como objetivo utilizar a raspagem de dados em um determinado site e salvar as informações em um banco de dados (Atlas MongoDB).
O site usado é o canal de noticias sobre de tecnologia [TecMundo](https://www.tecmundo.com.br/)

> Pontos a considerar:
> - O banco de dados utilizado é uma versão free, suporta apenas 20 coleções por database;
> - A URI está exposta no código. Entendo a falha de segurança aqui, porém, se trata de um BD free e sem dados sensíveis ;)



## Utilizando a aplicação:
- Clone o repositório

    `git clone https://github.com/palenske/tech-news_rapagem-de-dados.git`
- Entre na pasta do repositório que você acabou de clonar:

    `cd tech-news_rapagem-de-dados`
- Crie o ambiente virtual para o projeto

    `python3 -m venv .venv && source .venv/bin/activate`
- Instale as dependências

    `python3 -m pip install -r requirements.txt`
- Inicie o script `menu.py`:

    `python3 -i tech_news/scraping_menu.py`
- Por fim, chame a função que mostrará o menu para utilizar as funcionalidade da aplicação:

    *>>* `analyzer_menu()`

Terá uma saída parecida com esta:

```
    Selecione uma das opções a seguir:
    0 - Popular o banco com notícias;
    1 - Buscar notícias por título;
    2 - Buscar notícias por data;
    3 - Buscar notícias por fonte;
    4 - Buscar notícias por categoria;
    5 - Listar top 5 notícias;
    6 - Listar top 5 categorias;
    7 - Sair.
```
> Em breve montarei uma interface para usar essas funções em uma página HTML, sem precisar realizar os procedimentos acima 😉
---

## Habilidades

- Utilizar o terminal interativo do Python;
- Escrever seus próprios módulos e importá-los em outros códigos;
- Aplicar técnicas de raspagem de dados;
- Extrair dados de conteúdo HTML;
- Armazenar os dados obtidos em um banco de dados.

---
